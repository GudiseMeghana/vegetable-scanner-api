import os
import uvicorn
import numpy as np
import tensorflow as tf
import psycopg2
from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Function to connect to PostgreSQL
def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

# Function to create the products table (if it doesn't exist)
def create_products_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT UNIQUE,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def force_insert_products():
    conn = get_db_connection()
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM products;")

   
    vegetables = [
        ("Bean", 2.00), ("Bitter Gourd", 2.50), ("Bottle Gourd", 1.80),
        ("Brinjal", 2.30), ("Broccoli", 3.50), ("Cabbage", 1.50),
        ("Capsicum", 3.00), ("Carrot", 2.00), ("Cauliflower", 2.80),
        ("Cucumber", 1.80), ("Papaya", 2.50), ("Potato", 1.50),
        ("Pumpkin", 1.80), ("Radish", 2.20), ("Tomato", 2.50)
    ]

    cursor.executemany("INSERT INTO products (name, price) VALUES (%s, %s)", vegetables)
    conn.commit()
    conn.close()

#  Ensure the database is set up before running the API
create_products_table()
force_insert_products()  # This will run automatically when you deploy

# Function to fetch Product ID & Price
def get_product_details(vegetable_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, price FROM products WHERE name=%s", (vegetable_name,))
    product = cursor.fetchone()
    conn.close()
    
    if product:
        return {"product_id": product[0], "price_per_kg": product[1]}
    else:
        return {"product_id": None, "price_per_kg": None}

# Load trained model
model = tf.keras.models.load_model("vegetable_mobilenetv2_finetuned.h5")

# Define class labels
class_labels = ['Bean', 'Bitter Gourd', 'Bottle Gourd', 'Brinjal', 'Broccoli',
                'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber',
                'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']

# Image preprocessing function
def preprocess_image(image: Image.Image):
    img = image.resize((224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# API endpoint to predict vegetable
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        processed_img = preprocess_image(image)

        # Make prediction
        predictions = model.predict(processed_img)
        predicted_class = class_labels[np.argmax(predictions)]
        confidence = float(np.max(predictions))

        # Fetch Product ID & Price
        product_info = get_product_details(predicted_class)

        return {
            "vegetable": predicted_class,
            "confidence": confidence,
            "product_id": product_info["product_id"],
            "price_per_kg": product_info["price_per_kg"]
        }
    
    except Exception as e:
        return {"error": str(e)}

# API to manually check database records
@app.get("/show-products/")
def show_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        conn.close()

        return {"products": products}
    
    except Exception as e:
        return {"error": str(e)}

# Ensure correct port binding for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

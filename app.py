import os
import uvicorn
import numpy as np
import tensorflow as tf
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
    allow_origins=["*"],  # Replace * with frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Disable GPU usage for TensorFlow
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Root endpoint
@app.get("/")
def home():
    return {"message": "Vegetable Scanning API is running!"}

# Load trained model
model = tf.keras.models.load_model("vegetable_mobilenetv2_finetuned.h5")

# Define class labels
class_labels = ['Bean', 'Bitter Gourd', 'Bottle Gourd', 'Brinjal', 'Broccoli', 
                'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 
                'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']

# Hardcoded product details (Product ID & Price in ₹)
product_details = {
    'Bean': {"product_id": "V001", "price_per_kg": 40},
    'Bitter Gourd': {"product_id": "V002", "price_per_kg": 35},
    'Bottle Gourd': {"product_id": "V003", "price_per_kg": 25},
    'Brinjal': {"product_id": "V004", "price_per_kg": 30},
    'Broccoli': {"product_id": "V005", "price_per_kg": 70},
    'Cabbage': {"product_id": "V006", "price_per_kg": 20},
    'Capsicum': {"product_id": "V007", "price_per_kg": 60},
    'Carrot': {"product_id": "V008", "price_per_kg": 45},
    'Cauliflower': {"product_id": "V009", "price_per_kg": 28},
    'Cucumber': {"product_id": "V010", "price_per_kg": 22},
    'Papaya': {"product_id": "V011", "price_per_kg": 25},
    'Potato': {"product_id": "V012", "price_per_kg": 18},
    'Pumpkin': {"product_id": "V013", "price_per_kg": 20},
    'Radish': {"product_id": "V014", "price_per_kg": 30},
    'Tomato': {"product_id": "V015", "price_per_kg": 32}
}

# Image preprocessing function
def preprocess_image(image: Image.Image):
    img = image.resize((224, 224))  # Resize to model input size
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Prediction endpoint
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        processed_img = preprocess_image(image)

        # Make prediction
        predictions = model.predict(processed_img)
        predicted_class = class_labels[np.argmax(predictions)]
        confidence = round(float(np.max(predictions)) * 100, 2)  # Only multiply ONCE

        # Get product info
        details = product_details.get(predicted_class, {
            "product_id": "Not Found",
            "price_per_kg": "N/A"
        })

        return {
            "vegetable": predicted_class,
            "confidence": confidence,  # No extra multiplication
            "product_id": details["product_id"],
            "price_per_kg": f"₹{details['price_per_kg']}" if isinstance(details['price_per_kg'], int) else details['price_per_kg']
        }

    except Exception as e:
        return {"error": str(e)}

# Run locally or on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)

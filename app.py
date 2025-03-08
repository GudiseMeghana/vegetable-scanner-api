import uvicorn
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import io

# Initialize FastAPI app
app = FastAPI()

# Load trained model
model = tf.keras.models.load_model("vegetable_mobilenetv2_finetuned.h5")

# Define class labels
class_labels = ['Bean', 'Bitter Gourd', 'Bottle Gourd', 'Brinjal', 'Broccoli', 
                'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 
                'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']

# Image preprocessing function
def preprocess_image(image: Image.Image):
    img = image.resize((224, 224))  # Resize to model input size
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
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

        return {"vegetable": predicted_class, "confidence": confidence}
    
    except Exception as e:
        return {"error": str(e)}

# Run FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
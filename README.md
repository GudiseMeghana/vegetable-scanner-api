# 🌿 Vegetable Scanner API 🍅🥕🥦  

**An AI-powered web app that detects vegetables from images using deep learning.**  

## 🚀 Project Overview  
This project uses a **CNN model (MobileNetV2)** trained on a **Kaggle dataset** to classify vegetables.  
Users can **upload an image or use their webcam** to scan vegetables in real time.  

🔗 **Live API:** [https://vegetable-scanner-api.onrender.com/docs](https://vegetable-scanner-api.onrender.com/docs)  
🔗 **Live Frontend:** [https://vegetable-scanner.vercel.app](https://vegetable-scanner.vercel.app)  
🔗 **GitHub Repo:** [https://github.com/GudiseMeghana/vegetable-scanner-api](https://github.com/GudiseMeghana/vegetable-scanner-api)  

## Dataset

The dataset used for this project is the [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) from Kaggle.

- Dataset URL: [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)
- Description: This dataset contains images of various vegetables. It is used to train and test the vegetable scanner model.
---

## 📌 Table of Contents  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Examples](#examples)  
- [API Documentation](#api-documentation)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements](#acknowledgements)  

<h2 id="features">📌 Features</h2>

-  **Upload images to detect vegetables**  
-  **Live webcam scanning for real-time detection**  
-  **Confidence score for each prediction**  
-  **Database Integration (Product ID & Price)**
-  **FastAPI Backend & PostgreSQL Database**

<h2 id="tech-stack">🏗️ Tech Stack</h2>

- **Backend:** FastAPI (Python)  
- **Frontend:** HTML, CSS, JavaScript (Vercel)  
- **Model:** CNN (TensorFlow/Keras)  
- **Deployment:** Render (Backend) & Vercel (Frontend)  

<h2 id="installation">⚙️ Installation</h2>

1. **Clone the repository:**  
    ```sh  
    git clone https://github.com/GudiseMeghana/vegetable-scanner-api.git  
    cd vegetable-scanner-api  
    ```  
2. **Set up the backend:**  
    - Create a virtual environment:  
        ```sh  
        python -m venv venv  
        source venv/bin/activate  
        ```  
    - Install dependencies:  
        ```sh  
        pip install -r requirements.txt  
        ```
    - Run the backend server:  
        ```sh  
        uvicorn main:app --reload  
        ```  
4. **Set up the frontend:**  
    - Open `index.html` in your preferred browser.  

<h2 id="usage">🚀 Usage</h2>

- **Upload an image:** Click on the "Upload" button to upload an image of a vegetable.  
- **Use webcam:** Click on the "Capture Image" button to start real-time scanning.  
- **View results:** The detected vegetable and its confidence score will be displayed on the screen.  

<h2 id="examples">📸 Examples</h2>

- Example 1: Uploading an image of a tomato and getting the detection result.
  ![Tomato Detection]![WhatsApp Image 2025-03-11 at 18 27 37](https://github.com/user-attachments/assets/4cae324b-f89b-4aee-9f2e-e1ae62ccb164)


- Example 2: Using the webcam to scan a carrot in real time.
  ![Carrot Detection]https://drive.google.com/file/d/1B526w0cYuBpqVc4RRAtsBFl-AhH5hPSW/view?usp=sharing



<h2 id="api-documentation">📚 API Documentation</h2>

- **Endpoint:** `/predict`  
    - **Method:** `POST`  
    - **Description:** Upload an image to get the vegetable detection result.  
    - **Request Body:**  
        ```sh
        {
        curl -X 'POST' \
        'https://vegetable-scanner-api.onrender.com/predict/' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@images-3.jpeg;type=image/jpeg'
        }
        ```  
    - **Response:**  
        ```json
        {
            "vegetable": "Bitter Gourd",
            "confidence": 1,
            "product_id": 2,
            "price_per_kg": 2.5
        }  
        ```  

<h2 id="contributing">🤝 Contributing</h2>

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-name`  
3. Make your changes and commit them: `git commit -m 'Add new feature'`  
4. Push to the branch: `git push origin feature-name`  
5. Create a pull request.  

<h2 id="license">📜 License</h2>

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

<h2 id="acknowledgements">🙏 Acknowledgements</h2>

- Kaggle for providing the vegetable dataset.  
- TensorFlow/Keras for the deep learning framework.  
- FastAPI for the web framework.  
- Vercel for frontend hosting.  
- Render for backend hosting.  

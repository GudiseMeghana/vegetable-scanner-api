# 🌿 Vegetable Scanner API 🍅🥕🥦  

**An AI-powered web app that detects vegetables from images using deep learning.**  

## 🚀 Project Overview  
This project uses a **CNN model (MobileNetV2)** trained on a **Kaggle dataset** to classify vegetables.  
Users can **upload an image or use their webcam** to scan vegetables in real time.  

🔗 **Live API:** [https://vegetable-scanner-api.onrender.com](https://vegetable-scanner-api.onrender.com/docs)  
🔗 **Live Frontend:** [https://vegetable-scanner.vercel.app](https://vegetable-scanner.vercel.app)  
🔗 **GitHub Repo:** [https://github.com/GudiseMeghana/vegetable-scanner-api](https://github.com/GudiseMeghana/vegetable-scanner-api)  

---

## 📌 Table of Contents  
- [Features](#-features)  
- [Tech Stack](#-tech-stack)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Examples](#-examples)  
- [API Documentation](#-api-documentation)  
- [Contributing](#-contributing)  
- [License](#-license)  
- [Acknowledgements](#-acknowledgements)  

## 📌 Features  
- ✅ **Upload images to detect vegetables**  
- ✅ **Live webcam scanning for real-time detection**  
- ✅ **Confidence score for each prediction**  
- ✅ **Fast and lightweight API**  

## 🏗️ Tech Stack  
- **Backend:** FastAPI (Python)  
- **Frontend:** HTML, CSS, JavaScript (Vercel)  
- **Model:** CNN (TensorFlow/Keras)  
- **Deployment:** Render (Backend) & Vercel (Frontend)  

## ⚙️ Installation  
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
3. **Set up the frontend:**  
    - Open `index.html` in your preferred browser.  

## 🚀 Usage  
- **Upload an image:** Click on the "Upload" button to upload an image of a vegetable.  
- **Use webcam:** Click on the "Capture Image" button to start real-time scanning.  
- **View results:** The detected vegetable and its confidence score will be displayed on the screen.  

## 📸 Examples  
- Example 1: Uploading an image of a tomato and getting the detection result.  
- Example 2: Using the webcam to scan a carrot in real time.  

## 📚 API Documentation  
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
            "vegetable": "Tomato",  
            "confidence": 0.95  
        }  
        ```  

## 🤝 Contributing  
1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-name`  
3. Make your changes and commit them: `git commit -m 'Add new feature'`  
4. Push to the branch: `git push origin feature-name`  
5. Create a pull request.  

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## 🙏 Acknowledgements  
- Kaggle for providing the vegetable dataset.  
- TensorFlow/Keras for the deep learning framework.  
- FastAPI for the web framework.  
- Vercel for frontend hosting.  
- Render for backend hosting.  

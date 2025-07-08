<h1 align="center"><b>Vegetable Scanner API</b></h1>
<p align="center"> 
  <em>An AI-powered web app that detects vegetables from images using deep learning.</em>  
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Jupyter%20Notebook-F37626?logo=jupyter&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/HTML-FF5722?logo=html5&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Flutter-02569B?logo=flutter&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Dart-0175C2?logo=dart&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Render-46E3B7?logo=render&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/EXE-4B4B4B?logo=windows&logoColor=white&style=for-the-badge" />
</p>

## 🚀 Project Overview  
This project uses a **CNN model (MobileNetV2)** trained on a **Kaggle dataset** to classify vegetables.  
Users can **upload an image or use their webcam** to scan vegetables in real time.  

### 📱 **Multiple Platform Access:**
- **🌐 Web App:** Browser-based vegetable scanner with webcam support
- **📱 Mobile App:** Flutter-based Android/iOS app with camera integration and offline capabilities
- **🖥️ Desktop App:** EXE file for Windows users
- **🔧 API:** RESTful API for developers to integrate vegetable recognition into their apps  

🔗 **Live API:** [https://vegetable-scanner-api.onrender.com/docs](https://vegetable-scanner-api.onrender.com/docs)  
🔗 **Live Frontend:** [https://vegetable-scanner.vercel.app](https://vegetable-scanner.vercel.app)  
🔗 **GitHub Repo:** [https://github.com/GudiseMeghana/vegetable-scanner-api](https://github.com/GudiseMeghana/vegetable-scanner-api)  
📱 **Mobile App:** [Download APK](https://github.com/GudiseMeghana/vegetable-scanner-api/releases/latest/download/app-release.apk) | [App Source Code](./vegetable_scanner_app/)  
🖥️ **Desktop App:** [Download EXE](https://github.com/GudiseMeghana/vegetable-scanner-api/releases/latest/download/VegetableScanner.exe) | [App Source Code](./desktop_app/)  

## Dataset

The dataset used for this project is the [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset) from Kaggle.

- Dataset URL: [Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)
- Description: This dataset contains images of various vegetables. It is used to train and test the vegetable scanner model.
---

## 📌 Table of Contents  
- [Features](#features)  
- [Platform Access](#platform-access)
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
-  **📱 Mobile app with camera integration**

<h2 id="platform-access">📱 Platform Access</h2>

### 🌐 **Web Application**
- **Live Demo:** [https://vegetable-scanner.vercel.app](https://vegetable-scanner.vercel.app)

### 📱 **Mobile Application**
- **📲 Download APK:** [Get Android App](https://www.dropbox.com/scl/fi/r220e6jwtocnxe9zk66xs/LeafLense.apk?rlkey=xzrb3ln2dpk74lo4s2q8w6shn&st=1cm9j4g7&dl=1)
- **📂 Source Code:** [View App Folder](./vegetable_scanner_app/)
- **Requirements:** Android 5.0+

### 🖥️ **Desktop Application (Windows EXE)**
- **💻 Download EXE:** [Get Windows App](https://drive.google.com/file/d/1l70z8In9TtBMDf4u1CgnvCyMJ43qyCvJ/view?usp=sharing)
- **📂 Source Code:** [View Desktop App Folder](./vegetable_Scanner_exe/)
- **How to use:** Download the EXE and double-click to run on Windows 10/11. No installation required. If you see a security warning, click "More info" and then "Run anyway."

### 🔧 **Developer API**
- **API Docs:** [https://vegetable-scanner-api.onrender.com/docs](https://vegetable-scanner-api.onrender.com/docs)

<h2 id="tech-stack">🏗️ Tech Stack</h2>

### 🌐 **Web Application**
- **Backend:** FastAPI (Python)  
- **Frontend:** HTML, CSS, JavaScript (Vercel)  
- **Model:** CNN (TensorFlow/Keras)  
- **Deployment:** Render (Backend) & Vercel (Frontend)  

### 📱 **Mobile Application**
- **Framework:** Flutter (Dart)
- **Platform:** Android & iOS
- **State Management:** StatefulWidget
- **HTTP Client:** http package
- **Image Handling:** image_picker package
- **UI Components:** Material Design  

### 🖥️ **Desktop Application**
- **Framework:** PyInstaller (for EXE conversion)
- **Language:** Python
- **Dependencies:** Same as backend requirements

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
5. **Set up the mobile app:**  
    - Install Flutter SDK.
    - Open the project in Android Studio or VS Code.
    - Run `flutter pub get` to install dependencies.
    - Connect a device or start an emulator.
    - Run `flutter run` to launch the app.
6. **Set up the desktop app:**  
    - Install PyInstaller: `pip install pyinstaller`
    - Navigate to the desktop app folder: `cd desktop_app`
    - Build the EXE: `pyinstaller --onefile main.py`
    - Find the EXE in the `dist` folder.

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

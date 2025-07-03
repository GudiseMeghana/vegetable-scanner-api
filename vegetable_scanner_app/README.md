# 🥕 Vegetable Scanner App

A cross-platform Flutter app that identifies vegetables from an image using a FastAPI backend powered by a trained ML model.

### 📱 Features

- 📸 Take a photo or upload from gallery
- 🤖 Sends image to a FastAPI endpoint for prediction
- 📊 Displays predicted vegetable, confidence, product ID, and price
- 🎨 Polished UI with gradient buttons and cards
- ✅ Works on Android (and iOS Simulator or device via Xcode)

---

## 🚀 Getting Started

### 📦 Requirements

- Flutter 3.0 or higher
- Dart SDK
- Android Studio or VS Code with Flutter/Dart plugins
- Emulator or real device

### 🔧 Installation

1.  **Clone the repo**
    bash git clone https://github.com/GudiseMeghana/vegetable-scanner-app.git
    cd vegetable-scanner-app
2.  **Install dependencies**
    bash flutter pub get
3.  **Run the app**
    bash flutter run

---

## 🔗 API Integration

The app connects to a FastAPI backend deployed at:

[`https://vegetable-scanner-api.onrender.com/predict/`](https://vegetable-scanner-api.onrender.com/predict/)

- Uses `multipart/form-data` POST requests
- Receives structured JSON with:
- `vegetable`
- `confidence`
- `product_id`
- `price_per_kg`

---

## 📂 Folder Structure

lib/ ├── main.dart # Main UI and logic assets/
└── icon.png # App launcher icon android/ # Platform-specific code for Android

---

## 🧪 Testing

You can test on:

- Android Emulator
- Real Android phone (via APK)
- iPhone Simulator (via Xcode)
- Real iPhone (with Xcode provisioning)

---

## 📸 Screenshots

Below are screenshots of the app UI and prediction result. If the images do not display, ensure the files `ui.png` and `result.png` are present in the `screenshots/` folder (case-sensitive) and committed to your repository.

<p align="center">
  <img src="screenshots/ui.png" width="250" alt="App UI Screenshot"/>
  <img src="screenshots/result.png" width="250" alt="Prediction Result Screenshot"/>
</p>

---

## ✨ Future Improvements

- 🗣️ Add voice output for results
- 🔍 Add search by vegetable name
- 🛒 Integrate with vegetable marketplaces

---

## 👩‍💻 Developed By

Meghana Gudise,Rithvika Punnam,Vaagdevi Challa,Sankrishna Kuchana,Vishwajitha Byru,Pruthan Jamalapuram

---

## 📄 License

This project is licensed under the MIT License.

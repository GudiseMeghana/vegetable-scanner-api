import customtkinter as ctk
import tkinter.filedialog as fd
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

# TFLite setup
import sys, os
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS  # temp folder for PyInstaller
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

model_path = resource_path("vegetable_model.tflite")
interpreter = tf.lite.Interpreter(model_path=model_path)

interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

class_labels = ['Bean', 'Bitter Gourd', 'Bottle Gourd', 'Brinjal', 'Broccoli',
                'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber',
                'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']

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

# GUI setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("640x640")
app.title("Vegetable Scanner")

frame = ctk.CTkFrame(app, corner_radius=20)
frame.pack(padx=20, pady=20, expand=True, fill="both")

title = ctk.CTkLabel(frame, text="Vegetable Scanner AI", font=("Poppins", 24))
title.pack(pady=15)

preview_label = ctk.CTkLabel(frame, text="")
preview_label.pack(pady=10)

result_label = ctk.CTkLabel(frame, text="", font=("Poppins", 16), justify="left")
result_label.pack(pady=15)

def preprocess_image(img):
    img = img.resize((224, 224))
    img = np.expand_dims(np.array(img, dtype=np.float32) / 255.0, axis=0)
    return img

def predict_image(image):
    img = preprocess_image(image)
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    pred_index = int(np.argmax(output_data))
    confidence = round(float(np.max(output_data)) * 100, 2)
    label = class_labels[pred_index]
    details = product_details.get(label, {})
    return label, confidence, details

def reset_display():
    global cap
    if cap and cap.isOpened():
        cap.release()
        cap = None
    preview_label.configure(image="", text="")
    preview_label.image = None
    result_label.configure(text="")

def show_result(label, conf, info):
    result_label.configure(text=f"Vegetable: {label}\nConfidence: {conf}%\n"
                                f"Product ID: {info.get('product_id', '?')}\n"
                                f"Price per kg: ₹{info.get('price_per_kg', '?')}")
    result_label.after(5000, reset_display)

def display_image(img):
    img = img.resize((300, 300))
    tk_img = ImageTk.PhotoImage(img)
    preview_label.configure(image=tk_img, text="")
    preview_label.image = tk_img

cap = None
def classify_from_file():
    global cap
    if cap and cap.isOpened():
        cap.release()
        preview_label.configure(image="", text="")  # Clear old feed

    file_path = fd.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if not file_path:
        return
    img = Image.open(file_path)
    display_image(img)
    label, conf, info = predict_image(img)
    show_result(label, conf, info)

def start_camera():
    global cap
    if cap and cap.isOpened():
        cap.release()
    cap = cv2.VideoCapture(0)
    show_frame()

def show_frame():
    if cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            display_image(img)
        preview_label.after(100, show_frame)

def capture_and_classify():
    if cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            display_image(img)
            label, conf, info = predict_image(img)
            show_result(label, conf, info)


# Buttons
btn_upload = ctk.CTkButton(frame, text="Upload Image", command=classify_from_file)
btn_upload.pack(pady=10, ipadx=10, ipady=5)

btn_cam_start = ctk.CTkButton(frame, text="Start Camera", command=start_camera)
btn_cam_start.pack(pady=10, ipadx=10, ipady=5)

btn_cam_capture = ctk.CTkButton(frame, text="Scan Camera Frame", command=capture_and_classify)
btn_cam_capture.pack(pady=10, ipadx=10, ipady=5)

app.mainloop()

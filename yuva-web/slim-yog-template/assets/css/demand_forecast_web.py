import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from mtcnn import MTCNN

# Load the pre-trained model
model = load_model('C:\Users\kaviy\Downloads\improved_emotion_recognition_model.h5')

# List of emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Initialize the MTCNN face detector
detector = MTCNN()

def predict_emotion(img_path):
    try:
        image = cv2.imread(img_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

        # Detect faces in the image
        faces = detector.detect_faces(image_rgb)

        if faces:
            for face in faces:
                x, y, w, h = face['box']
                face_crop = image_rgb[y:y+h, x:x+w]  # Extract the face region

                # Convert face crop to grayscale, resize to 48x48, and preprocess
                face_crop_resized = cv2.resize(face_crop, (48, 48))
                face_crop_resized = face_crop_resized.astype('float32') / 255.0  # Normalize pixel values
                face_crop_resized = np.expand_dims(face_crop_resized, axis=0)  # Add batch dimension

                # Predict the emotion
                predictions = model.predict(face_crop_resized)
                max_index = np.argmax(predictions)
                emotion_label = emotion_labels[max_index]

                return emotion_label
        else:
            return "No face detected"
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Error in prediction"

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
    if file_path:
        result = predict_emotion(file_path)
        messagebox.showinfo("Prediction", f"The detected emotion is: {result}")
        display_image(file_path)

def display_image(img_path):
    try:
        img = Image.open(img_path)
        img = img.resize((int(camera_feed_label.winfo_width()), int(camera_feed_label.winfo_height())), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        camera_feed_label.config(image=img)
        camera_feed_label.image = img
    except Exception as e:
        print(f"Error displaying image: {e}")

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        camera_feed_label.config(image=img)
        camera_feed_label.image = img
    camera_feed_label.after(10, update_frame)

def activate_camera():
    if cap.isOpened():
        cap.release()
    cap.open(0)
    update_frame()

def capture_and_predict():
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            file_path = "captured_image.jpg"
            cv2.imwrite(file_path, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            result = predict_emotion(file_path)
            messagebox.showinfo("Prediction", f"The detected emotion is: {result}")

def display_image(img_path):
    try:
        img = Image.open(img_path)
        img = img.resize((int(camera_feed_label.winfo_width()), int(camera_feed_label.winfo_height())), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        camera_feed_label.config(image=img)
        camera_feed_label.image = img
    except Exception as e:
        print(f"Error displaying image: {e}")

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect faces in the frame
        faces = detector.detect_faces(frame_rgb)
        
        for face in faces:
            x, y, w, h = face['box']
            face_crop = frame_rgb[y:y+h, x:x+w]
            
            # Convert face crop to grayscale, resize, and preprocess
            face_crop_resized = cv2.resize(face_crop, (48, 48))
            face_crop_resized = face_crop_resized.astype('float32') / 255.0
            face_crop_resized = np.expand_dims(face_crop_resized, axis=0)
            
            # Predict the emotion
            predictions = model.predict(face_crop_resized)
            max_index = np.argmax(predictions)
            emotion_label = emotion_labels[max_index]
            
            # Draw rectangle around face
            cv2.rectangle(frame_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Put the emotion label text on the frame
            cv2.putText(frame_rgb, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Convert the frame to PIL image and update the label
        img = Image.fromarray(frame_rgb)
        img = ImageTk.PhotoImage(image=img)
        camera_feed_label.config(image=img)
        camera_feed_label.image = img
    
    camera_feed_label.after(10, update_frame)



# Create the main application window
root = tk.Tk()
root.title("Emotion Detection")
root.geometry("8000x6000")  # Set the window size

# Set up the layout with a stylish frame
frame = tk.Frame(root, bg='#2C3E50', bd=5, relief=tk.RAISED)
frame.place(relwidth=1, relheight=1)

# Add a gradient background
canvas = tk.Canvas(frame, width=800, height=600)
canvas.place(relx=0, rely=0)
gradient_image = tk.PhotoImage(width=8000, height=6000)
for i in range(600):
    color = f'#{int(44 + (255-44)*i/600):02x}{int(62 + (255-62)*i/600):02x}{int(80 + (255-80)*i/600):02x}'
    gradient_image.put(color, (0, i, 800, i+1))
canvas.create_image(0, 0, image=gradient_image, anchor="nw")

# Add a headline label at the top of the frame
headline_label = tk.Label(frame, text="Discover Emotions Instantly", bg='#2C3E50', fg='#ECF0F1', font=('Arial', 28, 'bold'))
headline_label.pack(pady=20)

# Add the camera feed section with a modern look
camera_feed_label = tk.Label(frame, bg='#34495E', bd=10, relief=tk.RIDGE, highlightthickness=5, highlightbackground='#2980B9')
camera_feed_label.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.7)

# Create a frame for the buttons with a stylish look
button_frame = tk.Frame(frame, bg='#2C3E50', bd=5, relief=tk.FLAT)
button_frame.place(relx=0.7, rely=0.3, relwidth=0.25, relheight=0.4)

# Add buttons for browsing, activating the camera, and capturing & predicting with modern design
button_style = {'bg': '#1ABC9C', 'fg': 'white', 'font': ('Arial', 14, 'bold'), 'relief': tk.FLAT, 'bd': 2}
browse_button = tk.Button(button_frame, text="Upload Image", command=browse_file, **button_style)
browse_button.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

camera_button = tk.Button(button_frame, text="Activate Camera", command=activate_camera, bg='#3498DB', fg='white', font=('Arial', 14, 'bold'), relief=tk.FLAT, bd=2)
camera_button.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

capture_button = tk.Button(button_frame, text="Capture & Predict", command=capture_and_predict, bg='#E74C3C', fg='white', font=('Arial', 14, 'bold'), relief=tk.FLAT, bd=2)
capture_button.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

# Open the camera
cap = cv2.VideoCapture(0)

# Run the Tkinter event loop
root.mainloop()

# Release the camera
cap.release()
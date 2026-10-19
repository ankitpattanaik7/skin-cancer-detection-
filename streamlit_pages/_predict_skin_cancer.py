import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load trained model
MODEL_PATH = "model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

CLASS_LABELS = ["Benign", "Malignant"]

st.title("🔬 Skin Cancer Detection - AI Model")
st.write("Upload an image to predict whether the lesion is **benign** or **malignant**.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    st.image(img, caption="Uploaded Image", width=300)

    # Predict
    prediction = model.predict(img_array)[0]
    class_idx = np.argmax(prediction)
    class_label = CLASS_LABELS[class_idx]
    confidence = float(prediction[class_idx]) * 100

    st.markdown(
        f'<div style="background-color:#E3F2FD; padding:10px; border-radius:10px; text-align:center; font-size:20px;">'
        f'Predicted: {class_label} <br> Confidence: {confidence:.2f}%</div>',
        unsafe_allow_html=True
    )

    if class_label == "Malignant":
        st.warning("⚠️ Consult a dermatologist for a professional opinion.")
    else:
        st.success("✅ The lesion appears benign, but regular check-ups are recommended.")

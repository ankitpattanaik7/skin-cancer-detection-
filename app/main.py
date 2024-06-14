from fastapi import FastAPI, UploadFile, File, HTTPException
import tensorflow as tf
from PIL import Image, UnidentifiedImageError
import io
from pathlib import Path

app = FastAPI(title="Skin Lesion Classification")

def load_model():
    model_path = Path(__file__).resolve().parent.parent / "weights" / "EfficientNetB2.h5"
    model = tf.keras.models.load_model(model_path)
    return model

def load_and_preprocess_image(image_bytes):
    image = tf.image.decode_image(image_bytes, channels=3)
    image = tf.image.resize(image, [260, 260])
    image = image / 255.0
    return image

def predict_image(model, image_bytes):
    label_mapping = {"MEL":"Melanoma", "NV":"Melanocytic nevus", "BCC":"Basal cell carcinoma", "AK":"Actinic keratosis", 
    "BKL":"Benign Keratosis", "DF":"Dermatofibroma", "VASC":"Vascular lesion", "SCC":"Squamous cell carcinoma"}
    
    image = load_and_preprocess_image(image_bytes)
    image = tf.expand_dims(image, axis=0)
    predictions = model.predict(image)
    predicted_label = tf.argmax(predictions, axis=1)[0]
    predicted_label = predicted_label.numpy()
    
    return {'id': int(predicted_label), 
            'key': list(label_mapping)[predicted_label],
            'label': str(label_mapping[list(label_mapping)[predicted_label]]).title(),
            'confidence': float(predictions[0][predicted_label])}

@app.get("/")
def display() -> str:
    return "Beep Beep!"

@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> dict:
    model = load_model()
    image_bytes = await file.read()
    
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image.verify()
        preds_label = predict_image(model, image_bytes)
        return preds_label
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="The uploaded file is not a valid image.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
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
    LABEL_MAP = {
        "MEL":{
                "label":"Melanoma",
                "description": "Melanoma is a skin cancer that is characterized by the presence of melanocytes, which are cells that produce melanin.",
                "link": "https://en.wikipedia.org/wiki/Melanoma"
        },
        "NV":{
                "label":"Melanocytic nevus",
                "description": "A melanocytic nevus is a benign skin lesion that is characterized by the presence of melanocytes. It is often found on the face, neck, and scalp.",
                "link": "https://en.wikipedia.org/wiki/Melanocytic_nevus"
        }, 
        "BCC":{
                "label":"Basal cell carcinoma",
                "description": "Basal cell carcinoma is a type of skin cancer that is characterized by the presence of basal cells, which are cells that do not have a clear cell type.",
                "link": "https://en.wikipedia.org/wiki/Basal_cell_carcinoma"
        }, 
        "AK":{
                "label":"Actinic keratosis",
                "description": "Actinic keratosis is a skin condition that is characterized by the presence of red, white, or yellow-brown patches on the skin. It is often caused by exposure to ultraviolet (UV) radiation.",
                "link": "https://en.wikipedia.org/wiki/Actinic_keratosis"
        }, 
        "BKL":{
                "label":"Benign Keratosis",
                "description": "Benign keratosis is a skin condition that is characterized by the presence of red, white, or yellow-brown patches on the skin. It is often caused by exposure to ultraviolet (UV) radiation.",
                "link": "https://en.wikipedia.org/wiki/Benign_keratosis"
        }, 
        "DF":{
                "label":"Dermatofibroma",
                "description": "Dermatofibroma is a skin cancer that is characterized by the presence of dermal fibroblasts, which are cells that are found on the skin.",
                "link": "https://en.wikipedia.org/wiki/Dermatofibroma"
        }, 
        "VASC":{
                "label":"Vascular lesion",
                "description": "Vascular lesion is a skin condition that is characterized by the presence of blood vessels on the skin. It is often caused by exposure to ultraviolet (UV) radiation.",
                "link": "https://en.wikipedia.org/wiki/Vascular_lesion"
        }, 
        "SCC":{
                "label":"Squamous cell carcinoma",
                "description": "Squamous cell carcinoma is a type of skin cancer that is characterized by the presence of squamous cells, which are cells that have a clear cell type.",
                "link": "https://en.wikipedia.org/wiki/Squamous_cell_carcinoma"
        }
    }
    
    image = load_and_preprocess_image(image_bytes)
    image = tf.expand_dims(image, axis=0)
    predictions = model.predict(image)
    predicted_label = tf.argmax(predictions, axis=1)[0]
    predicted_label = predicted_label.numpy()
    key_ = list(LABEL_MAP)[predicted_label]
    
    return {'id': int(predicted_label), 
            'key': key_,
            'confidence': float(predictions[0][predicted_label]),
            'label': LABEL_MAP[key_]['label'],
            'description': LABEL_MAP[key_]['description'],
            'link': LABEL_MAP[key_]['link'],
        }

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
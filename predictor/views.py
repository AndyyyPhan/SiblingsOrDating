from django.shortcuts import render
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'siblings_or_dating_model.keras')
model = load_model(MODEL_PATH)

def preprocess_image(image_file):
    image = Image.open(image_file).convert('RGB')
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    return image_array.reshape(1, 224, 224, 3)

def home(request):
    prediction = None
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        processed = preprocess_image(image)
        result = model.predict(processed)[0][0]
        label = "Dating" if result >= 0.5 else "Siblings"
        confidence = f"{result:.2f}" if label == "Dating" else f"{1 - result:.2f}"
        prediction = f"{label} (Confidence: {confidence})"
    return render(request, 'predictor/home.html', {'prediction': prediction})

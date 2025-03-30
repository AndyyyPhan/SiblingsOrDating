# 🧠 Siblings or Dating? | ML-Powered Image Classifier

A web application that predicts whether a pair of people in a photo are **siblings** or **dating**, using a Convolutional Neural Network (CNN) trained on real Reddit data.

> Built for [HooHacks 2025]  
> Created by [Andy Phan] & [Sanjay Karunamoorthy]

---

## 💡 Inspiration

Inspired by the viral “Siblings or Dating?” meme and subreddit, we wanted to see if a machine learning model could learn to distinguish the subtle visual differences between family and romantic connections — from facial features to posture and expressions.

---

## 🚀 Features

- 🔍 Upload an image and get an instant prediction
- 🤖 CNN model trained on images scraped from Reddit
- 📸 Image preview before submitting
- 🌐 Django + TensorFlow backend
- 🎨 Bootstrap-styled web interface

---

## 🧪 Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Backend + ML |
| 🧠 TensorFlow/Keras | Model training |
| 🧬 CNN | For image classification |
| 🌐 Django | Web framework |
| 🎨 Bootstrap | Frontend styling |
| 🧾 Pillow | Image preprocessing |
| 🕵️‍♀️ BeautifulSoup / PRAW | Reddit scraping (optional) |

---

## 🧠 How it works

1. User uploads a photo with two people
2. The image is resized and preprocessed
3. The model predicts a probability score (siblings vs. dating)
4. Result and confidence score are shown

---

## 🛠️ Setup (Local)

1. Clone the repo

```bash
git clone https://github.com/AndyyyPhan/SiblingsOrDating.git
cd SiblingsOrDating

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Create a .env file with your Django secret key
echo DJANGO_SECRET_KEY=your-secret-key-here > .env

# Run the server
python manage.py migrate
python manage.py runserver
```

---

## 📓 Model Notebook

The full training process is documented in [`SiblingsOrDating.ipynb`](SiblingsOrDating.ipynb), including:

- Data scraping from Reddit
- Image preprocessing
- CNN architecture (MobileNetV2)
- Training + validation performance

---

## 🤝 Collaborators

- [@AndyyyPhan](https://github.com/AndyyyPhan)
- [@SanjayKarun4444](https://github.com/SanjayKarun4444)

---

## 📜 License

MIT — feel free to use, fork, or remix with credit!


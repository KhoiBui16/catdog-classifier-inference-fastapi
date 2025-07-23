
# 🐶🐱 Cat vs Dog Classifier API - FastAPI Deployment

A Deep Learning image classification model for Cats and Dogs using PyTorch and FastAPI, achieving around 60% accuracy. 
Users can upload images and receive classification results via a REST API.

---

## 🎯 Objectives

- Train a Cat/Dog image classification model using ResNet18 (pre-trained).

- Build a RESTful API with FastAPI to serve the model.

- Allow users to send images and get prediction results.

--- 



## 📁 Project Structure

```
catdog-classifier-inference-fastapi/
│
├── app.py                        # Initialize FastAPI app
├── server.py                     # Launch server with Uvicorn
├── requirements.txt              # Dependency list
├── animal_classification.ipynb   # Model training notebook
│
├── config/
│   ├── catdog_cfg.py             # Model & image preprocessing config
│   └── logging_cfg.py            # Logging config
│
├── logs/                         # Log files
│
├── middleware/
│   ├── __init__.py
│   ├── cors.py                   # CORS configuration
│   └── http.py                   # Log HTTP request
│
├── models/
│   ├── weights/
│   │   └── catdog_weights.pt     # Trained model weights
│   ├── catdog_model.py           # Model architecture
│   └── catdog_predictor.py       # Predictor class
│
├── routes/
│   ├── base.py                   # Route aggregator
│   └── catdog_route.py           # Route aggregator
│
├── schemas/
│   └── catdog_schema.py          # Response schema definition
│
└── utils/
    └── logger.py                 # Logger setup
```

---

## 🚀 Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/KhoiBui16/catdog-classifier-inference-fastapi.git
cd catdog-classifier-inference-fastapi
```


### 2. Create a Virtual Environment (Optional but Recommended)

**Using venv:**

```bash
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
```

**Using conda:**

```bash
conda create -n catdog_env python=3.10
conda activate catdog_env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Application

```bash
python server.py
```

- API will be **hosted at**: `http://0.0.0.0:8000`

- **Swagger UI**: `http://localhost:8000/docs`

---

## 🧠 Model Overview

- Architecture: ResNet18 pre-trained on ImageNet.

- Dataset: cats_vs_dogs from HuggingFace Datasets.

- Input: RGB image, resized to 64x64, normalized using ImageNet stats.

- Output: Softmax probabilities for Cat or Dog class.

- Accuracy: ~60% on validation set.

---

## 📸 API Endpoint

| Method | Endpoint                              | Description                            |
|--------|---------------------------------------|----------------------------------------|
| POST   | `/catdog_classification/predict`      | Upload an image and get prediction     |

**Request:**
- Type: multipart/form-data

- Field: file_upload (JPG, PNG...)

**Response (JSON):**
```json
{
  "probs": [0.41, 0.59],
  "best_prob": 0.59,
  "predicted_id": 1,
  "predicted_class": "Dog",
  "predictor_name": "resnet18"
}
```

---

## 🧪 Testing the API

Once server.py is running:

1. Visit: `http://localhost:8000/docs`

2. Use the /catdog_classification/predict endpoint

3. Upload an image and click "Execute" to view the result

---

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PyTorch](https://pytorch.org/)
- [HuggingFace Datasets](https://huggingface.co/datasets/cats_vs_dogs)

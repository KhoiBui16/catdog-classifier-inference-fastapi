
# 🐶🐱 Cat vs Dog Classifier API - FastAPI Deployment

Triển khai mô hình Deep Learning phân loại ảnh **Chó** và **Mèo** bằng **PyTorch** và **FastAPI**, đạt độ chính xác khoảng **60%**, cho phép người dùng tải ảnh và nhận kết quả phân loại thông qua REST API.

---

## 🎯 Mục tiêu

- Huấn luyện mô hình phân loại ảnh Cat/Dog bằng ResNet18 (pre-trained).
- Xây dựng RESTful API bằng FastAPI để phục vụ mô hình.
- Cho phép người dùng gửi ảnh và nhận kết quả dự đoán.

--- 



## 📁 Cấu trúc thư mục

```
catdog-classifier-inference-fastapi/
│
├── app.py                        # Khởi tạo app FastAPI
├── server.py                     # Chạy server bằng Uvicorn
├── requirements.txt              # Danh sách thư viện
├── animal_classification.ipynb   # File train model
│
├── config/
│   ├── catdog_cfg.py             # Config mô hình & xử lý ảnh
│   └── logging_cfg.py            # Config log
│
├── logs/                         # Thư mục lưu file log
│
├── middleware/
│   ├── __init__.py
│   ├── cors.py                   # Cấu hình CORS
│   └── http.py                   # Log HTTP request
│
├── models/
│   ├── weights/
│   │   └── catdog_weights.pt     # Trọng số mô hình đã train
│   ├── catdog_model.py           # Kiến trúc model
│   └── catdog_predictor.py       # Predictor class
│
├── routes/
│   ├── base.py                   # Gom tất cả route
│   └── catdog_route.py           # Định nghĩa API predict
│
├── schemas/
│   └── catdog_schema.py          # Định nghĩa dữ liệu response
│
└── utils/
    └── logger.py                 # Định nghĩa logger
```

---

## 🚀 Hướng dẫn chạy local

### 1. Clone project từ GitHub

```bash
git clone https://github.com/KhoiBui16/catdog-classifier-inference-fastapi.git
cd catdog-classifier-inference-fastapi
```


### 2. Tạo môi trường ảo (tuỳ chọn nhưng khuyến khích)

**Với venv:**

```bash
python -m venv venv
source venv/bin/activate        # Windows: .\venv\Scripts\activate
```

**Hoặc dùng conda:**

```bash
conda create -n catdog_env python=3.10
conda activate catdog_env
```

### 3. Cài đặt thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

### 4. Chạy ứng dụng FastAPI

```bash
python server.py
```

- API sẽ được host tại: `http://0.0.0.0:8000`
- Giao diện tương tác: `http://localhost:8000/docs`

---

## 🧠 Mô hình

- Sử dụng `ResNet18` đã được pre-trained trên ImageNet.
- Bộ dữ liệu: `cats_vs_dogs` từ HuggingFace Datasets.
- Input ảnh: RGB, resize 64x64, normalize chuẩn ImageNet.
- Output: lớp `Cat` hoặc `Dog`, xác suất softmax.
- Accuracy khoảng **60%** trên tập validation.

---

## 📸 API Endpoint

| Method | Endpoint                              | Mô tả                                 |
|--------|---------------------------------------|----------------------------------------|
| POST   | `/catdog_classification/predict`      | Nhận ảnh tải lên và trả về kết quả phân loại |

**Request:**
- Dạng: multipart/form-data
- Trường: `file_upload` (ảnh định dạng JPG, PNG...)

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

## 🧪 Kiểm tra API

Sau khi chạy `server.py`, bạn có thể:

1. Truy cập: [http://localhost:8000/docs](http://localhost:8000/docs)
2. Sử dụng endpoint `/catdog_classification/predict`
3. Upload một ảnh và nhấn "Execute" để xem kết quả.

---

## 📚 Tham khảo

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PyTorch](https://pytorch.org/)
- [HuggingFace Datasets](https://huggingface.co/datasets/cats_vs_dogs)

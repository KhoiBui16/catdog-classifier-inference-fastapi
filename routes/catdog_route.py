import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from fastapi import File, UploadFile
from fastapi import APIRouter
from schemas.catdog_schema import CatDogResponse
from config.catdog_cfg import ModelConfig
from models.catdog_predictor import Predictor


""" 
    Một API có thể sẽ có nhiều những chức năng khác nhau, từviệc truy vấn dữ liệu trong một database đến inference các Deep Learning model khác nhau.Vì vậy, để phân biệt rõ các chức năng trong một API, chúng ta cần định nghĩa các APIendpoints
    
    Trong demo này, chúng ta sẽ chỉ có một endpoint với chức năng inference model Cat DogClassification

    khởi tạo instance router của FastAPI để định nghĩa một endpoint, đồngthời khởi tạo một instance Predictor của model Cat Dog Classification để router này cóthể gọi và lấy kết quả dự đoán
"""

# Định nghĩa các endpoint
router = APIRouter()
predictor = Predictor(
    model_name=ModelConfig.MODEL_NAME,
    model_weight=str(ModelConfig.MODEL_WEIGHT),
    device=ModelConfig.DEVICE
)

@router.post("/predict")

async def preidct(file_upload: UploadFile = File(...)):
    response = await predictor.predict(file_upload.file)

    return CatDogResponse(**response)

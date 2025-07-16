from pydantic import BaseModel

class CatDogResponse(BaseModel):
    probs: list = []
    best_prob: float = -1.0
    predicted_id: int = -1
    predicted_class: str = ""
    predicted_name: str = ""
    
""" 
    Trong FastAPI, chúng ta có thể sử dụng Pydantic Model, một dạng data validation. PydanticModel cho phép chúng ta định nghĩa cấu trúc dữ liệu và đảm bảo rằng cấu trúc này sẽ luônđược tuân thủ bởi API. Đối với bài này, chúng ta sẽ cho người dùng gửi một tấm ảnh và API sẽ trả về kết quả dự đoán của tấm ảnh dưới dạng dictionary (JSON)

    Việc tạo pydantic model gần như tương tự với việc tạo một class trong Python, điểm khácbiệt là bạn cần phải cho kế thừa class BaseModel.
"""
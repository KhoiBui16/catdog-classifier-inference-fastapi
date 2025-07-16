from fastapi import APIRouter
from .catdog_route import router as catdog_cls_route


router = APIRouter()
router.include_router(catdog_cls_route, prefix="/catdog_classfication")


"""
    Trong trường hợp các bạn có nhiều router, chúng ta có thể tạo một file.py để import tất cả router của từng file và gom lại thành một router duy nhất. Trongtrường hợp này, mặc dù vậy, chúng ta sẽ chỉ import một router:
"""
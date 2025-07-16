import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI
from middleware import LogMiddleware, setup_cors
from routes.base import router


"""  
    khởi tạo mộtthực thể FastAPI để host API của chúng ta.
    tạo instance FastAPI với tên biến app, sau đó cập nhật middlware cũng như router màta đã định nghĩa ở các file khác vào trong biến này
"""

app = FastAPI()

app.add_middleware(LogMiddleware)
setup_cors(app)
app.include_router(router)



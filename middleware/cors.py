# cho phép tất cả orginj được quyền request và response
from starlette.middleware.cors import CORSMiddleware


# hàm này sẽ nhận input là thực thể của FastAPI -> đưa hàm này để cập nhật policy
def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
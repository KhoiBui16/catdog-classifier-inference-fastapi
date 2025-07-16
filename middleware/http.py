import time
import sys

from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from utils.logger import Logger

LOGGER = Logger(__file__, log_file="http.log")


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()
        processed_time = end_time - start_time
        client_host = request.client.host if request.client else "unknown"
        LOGGER.log.info(
            f"{client_host} - \"{request.method} {request.url.path} {request.scope["http_version"]}\"  {response.status_code} {processed_time:.2f}s"
        )

        return response
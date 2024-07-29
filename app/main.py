from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI, status
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse



from app.api.v1.router import router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> any:
    print(f"System start in : {datetime.now(settings.TIMEZONE)}")
    yield
    print(f"System shutdown in : {datetime.now(settings.TIMEZONE)}")


params = {
    'title': 'FastAPI Test 26/07/2024',
    'docs_url': '/',
    'lifespan': lifespan
}

app = FastAPI(**params)

app.include_router(router)

@app.exception_handler(IntegrityError)
async def integrity_error_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": "nickname already in use"},
    )
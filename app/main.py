from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI
from datetime import datetime

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
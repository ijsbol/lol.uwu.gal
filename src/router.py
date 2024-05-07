from contextlib import asynccontextmanager
from typing import List, Tuple

from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from routers.ip_memes.router import router as ip_memes_router


@asynccontextmanager
async def lifecycle(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifecycle,
)


app.mount("/static", StaticFiles(directory="static"), name="static")


routers: List[Tuple[APIRouter, str]] = [
    (ip_memes_router, "/v"),
]


for router, prefix in routers:
    app.include_router(router, prefix=prefix)

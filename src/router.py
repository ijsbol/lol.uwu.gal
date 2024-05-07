from contextlib import asynccontextmanager
from typing import Any, List, Tuple

from fastapi import APIRouter, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.templating import (
    _TemplateResponse,  # pyright: ignore[reportPrivateUsage]
)

from routers.ip_memes.router import router as ip_memes_router
from utils.config import ENABLED_MEMES, templates

@asynccontextmanager
async def lifecycle(app: FastAPI):
    yield


app = FastAPI(lifespan=lifecycle)


app.mount("/static", StaticFiles(directory="static"), name="static")


routers: List[Tuple[APIRouter, str]] = [
    (ip_memes_router, "/v"),
]


for router, prefix in routers:
    app.include_router(router, prefix=prefix)


@app.get("/")
async def home_page(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(
        name="home_page.jinja",
        context={
            "request": request,
            "subpages": [
                {
                    "link": f"v/{uri}",
                    "name": ENABLED_MEMES[uri]["name"],
                } for uri in ENABLED_MEMES
            ]
        },
    )


@app.exception_handler(404)
async def custom_404_handler(request: Request, *_: Any, **__: dict[str, Any]) -> _TemplateResponse:
    return templates.TemplateResponse(
        name="404.jinja",
        context={"request": request},
        status_code=404,
    )


@app.exception_handler(503)
async def custom_503_handler(request: Request, *_: Any, **__: dict[str, Any]) -> _TemplateResponse:
    return templates.TemplateResponse(
        name="503.jinja",
        context={"request": request},
        status_code=503,
    )

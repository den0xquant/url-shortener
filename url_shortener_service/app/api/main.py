from fastapi import APIRouter
from app.api.routes import (
    utils,
    urls,
)


api_router = APIRouter(tags=["api"])
api_router.include_router(utils.router)
api_router.include_router(urls.router) 

from fastapi import APIRouter
from app.api.routes import (
    utils,
)


api_router = APIRouter(tags=["api"])
api_router.include_router(utils.router)

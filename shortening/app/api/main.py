from fastapi import APIRouter
from app.api.routes import (
    auth,
    users,
    utils,
)


api_router = APIRouter(tags=["api"])
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)

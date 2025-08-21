from fastapi import APIRouter

from app.core.db import url_collection
from app.schemas.domain import ShortURLCreate


router = APIRouter(prefix="/urls", tags=["urls"])


@router.post("/shorten")
async def shorten_url(url: ShortURLCreate):
    url_data = url.model_dump()
    result = await url_collection.insert_one({"url": url_data})
    return {"shortened_url": str(result.inserted_id), "data": url_data}

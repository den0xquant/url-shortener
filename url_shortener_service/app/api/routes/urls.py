from fastapi import APIRouter

from app.schemas.domain import ShortURLCreate
from app.services import urls as url_service
from app.api.deps import RedisClientDep


router = APIRouter(prefix="/urls", tags=["urls"])


@router.post("/shorten")
async def shorten_url(url: ShortURLCreate, redis_client: RedisClientDep):
    url_data = url.model_dump()
    result = await url_service.shorten_url(
        long_url=url_data["long_url"],
        redis_client=redis_client,
    )
    return {"shortened_url": str(result), "data": url_data}

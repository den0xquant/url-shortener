import logging

from redis.asyncio import Redis

from app.core.config import settings
from app.core.db import urls_collection
from app.services.base62 import encode


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


async def get_next_id(redis_client: Redis) -> int:
    """Get the next unique ID from Redis counter."""
    return await redis_client.incr(settings.REDIS_COUNTER_KEY)


async def save_url(redis_client: Redis, short_url: str, long_url: str):
    """Save the short-long URL mapping to MongoDB and cache in Redis."""
    await urls_collection.insert_one({"short_url": short_url, "long_url": long_url})
    await redis_client.set(settings.REDIS_CACHE_PREFIX + short_url, long_url)


async def shorten_url(*, long_url: str, redis_client: Redis) -> str:
    """Shorten a URL and store mapping."""
    next_id = await get_next_id(redis_client)
    short_url = encode(next_id)
    await save_url(redis_client, short_url, long_url)
    return short_url

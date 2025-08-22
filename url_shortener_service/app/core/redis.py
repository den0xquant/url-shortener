import redis.asyncio as redis
from app.core.config import settings


def build_redis() -> redis.ConnectionPool:
    return redis.ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB
    )

pool = build_redis()

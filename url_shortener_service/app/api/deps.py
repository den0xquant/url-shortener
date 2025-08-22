import redis.asyncio as redis
from typing import Annotated
from fastapi import Depends

from app.core.redis import pool


def get_redis_client():
    return redis.Redis(
        connection_pool=pool,
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5,
    )


RedisClientDep = Annotated[redis.Redis, Depends(get_redis_client)]

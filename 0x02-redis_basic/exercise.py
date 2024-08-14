#!/usr/bin/env python3
"""
Cache class. In the __init__ method, store an instance of the Redis client
as a private variable named _redis (using redis.Redis())
and flush the instance using flushdb
"""

import redis
from typing import Union, Callable
from functools import wraps
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using the following
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

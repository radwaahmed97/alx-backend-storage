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

    def get(self, key: str, fn: Callable = None)\
            -> Union[str, bytes, int, float]:
        """
        Convert the data back to the desired format
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """
        Convert bytes to str
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """
        Convert bytes to int
        """
        return int(data)

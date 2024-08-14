#!/usr/bin/env python3
"""tracking how many times a url accessed"""
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()


def tracker_decorator(method: Callable) -> Callable:
    """tracking how many times a url been accessed"""
    @wraps(method)
    def wrapper(url) -> str:
        """wrapper method"""
        r.incr(f'count:{url}')
        res = r.get(f'result:{url}')
        if res:
            return res.decode('utf-8')
        res = method(url)
        r.set(f'count:{url}', 0)
        r.setex(f'result:{url}', 10, res)
        return res
    return wrapper


@tracker_decorator
def get_page(url: str) -> str:
    """get page content"""
    return requests.get(url).text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')

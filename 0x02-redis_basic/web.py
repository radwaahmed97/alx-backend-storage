#!/usr/bin/env python3
"""web module for caching web content and counting access for given url"""


import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def counting_Access_decorator(method: Callable) -> Callable:
    """decorator for get_page function"""
    @wraps(method)
    def wrapper(url) -> str:
        """wrapper function"""
        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        key_count = "count:" + url
        html_content = method(url)

        r.incr(key_count)
        r.set(key, html_content, ex=10)
        r.expire(key, 10)
        return html_content
    return wrapper


@counting_Access_decorator
def get_page(url: str) -> str:
    """get HTML content of a particular url"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')

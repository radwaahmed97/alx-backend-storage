#!/usr/bin/env python3
"""get_page function (prototype: def get_page(url: str) -> str:)"""

import redisplay
from functools import wraps
import requests

r = redis.Redis()


def count_url_access(method):
    """ return how many times a URL is accessed """
    @wraps(method)
    def wrapper(url):
        cach_key = "cached:" + url
        cach_data = r.get(cach_key)
        if cach_data:
            return cach_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        r.incr(count_key)
        r.set(cach_key, html)
        r.expire(cach_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML content of a
    particular URL and returns it.
    """
    return_url = requests.get(url)
    return return_url.text
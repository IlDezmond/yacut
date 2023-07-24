import hashlib
import random
from .models import URLMap
import re


def generate_short_link(url, link_length=6):
    hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    while True:
        short = ''.join([random.choice(hash) for _ in range(link_length)])
        if URLMap.short_link_not_exists(short):
            break
    return short


def regex_short_link_validate(url):
    return re.match(r'^[a-zA-Z0-9]{2,16}$', url)

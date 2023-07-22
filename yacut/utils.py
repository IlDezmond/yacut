import hashlib
import random
from .models import URLMap
import re


def generate_short_link(url):
    hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    short = ''.join([random.choice(hash) for _ in range(6)])
    while not URLMap.short_link_not_exists(short):
        short = ''.join([random.choice(hash) for _ in range(6)])
    return short


def regex_short_link_validate(url):
    return re.match(r'^[a-zA-Z0-9]{2,16}$', url)

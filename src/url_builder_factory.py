from typing import Optional
from url_builder import UrlBuilder


def CreateUrlBuilder(base_url: str) -> UrlBuilder:
    return UrlBuilder(base_url)

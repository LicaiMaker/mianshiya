#!/usr/bin/env python3
"""关键词匹配：ASCII 关键词走词边界正则，CJK 关键词走子串匹配。

避免 "ref" 命中 "reference"、"React" 命中 "reactive" 这类误匹配。
"""
import re

_ASCII_CACHE = {}


def _ascii_pattern(keyword):
    pattern = _ASCII_CACHE.get(keyword)
    if pattern is None:
        pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(keyword) + r"(?![A-Za-z0-9])", re.IGNORECASE)
        _ASCII_CACHE[keyword] = pattern
    return pattern


def match_keyword(title, keyword):
    low = keyword.lower()
    if low.isascii():
        return bool(_ascii_pattern(low).search(title))
    return low in title


def matches_keywords(title, keywords):
    return any(match_keyword(title, kw) for kw in keywords)

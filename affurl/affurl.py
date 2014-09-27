# -*- coding: utf-8 -*-
from urllib import urlencode
from urlparse import parse_qs, urlsplit, urlunsplit

from domain_parser import domain_parser


def convert(url, mapping):
    '''Convert given URL into affiliate URL based on mapping.

    mapping maps domains with URL query paramater/value pairs to add or replace
    in given URL. Parameter values must be specified as lists.

    Example mapping for various amazon domains:
        {
            'amazon.com': {'tag': ['affurl-20']},
            'amazon.de': {'tag': ['affurl-21']},
            'amazon.co.uk': {'tag': ['afflink-21']}
        }
    '''

    new_url = urlsplit(url)
    if not new_url.netloc:
        return None  # rather raise an Exception?

    # Parse_domain returns a tuple like ('co.uk', 'amazon', 'www').
    domain = '.'.join(domain_parser.parse_domain(new_url.netloc)[:2][::-1])

    # Leave URLs with no matching domain as they are.
    if domain not in mapping:
        return url

    # Add new and replace existing query paramters with given ones.
    query = parse_qs(new_url.query)
    params = mapping[domain]
    query.update(params)

    # Concatenate and unsplit tuples to create a URL string.
    return urlunsplit(new_url[:3] + (urlencode(query, True), ) + new_url[4:])
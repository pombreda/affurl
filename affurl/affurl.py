# -*- coding: utf-8 -*-
from urllib import urlencode
from urlparse import parse_qs, urlparse, urlunparse
from domain_parser import domain_parser


def convert(url, mapping):
    '''Convert given URL into affiliate URL based on mapping.

    mapping maps domains with URL paramater/value pairs to add or replace in
    given URL. Parameter values must be specified as lists.

    Example mapping for various amazon domains:
        {
            'amazon.com': {'tag': ['affurl-20']},
            'amazon.de': {'tag': ['affurl-21']},
            'amazon.co.uk': {'tag': ['afflink-21']}
        }
    '''

    new_url = urlparse(url)
    if not new_url.netloc:
        return None  # rather raise an Exception?

    # Parse_domain returns a tuple like ('co.uk', 'amazon', 'www')
    domain = '.'.join(domain_parser.parse_domain(new_url.netloc)[:2][::-1])

    # Leave URLs with no matching domain as they are
    if domain not in mapping:
        return url

    params = mapping[domain]

    # make sure this is a product URL. FIXME why is this important, which URLs
    # do not work when tag param is added? Maybe because in the previous
    # version all other params were removed?

    # if '/dp/' not in new_url.path and '/gp/product/' not in new_url.path:
    #     return url

    q = parse_qs(new_url.query)
    q.update(params)
    new_url = new_url[:4] + (urlencode(q, True), ) + new_url[5:]

    return urlunparse(new_url)
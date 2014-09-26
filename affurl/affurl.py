# -*- coding: utf-8 -*-

def convert(url, mapping):
    '''Convert given URL into affiliate URL based on mapping.

    mapping maps domains with URL paramater/value pairs to add or replace in
    given URL.

    Example mapping for various amazon domains:
        {
            'amazon.com': {'tag': 'affurl-20'},
            'amazon.de': {'tag': 'affurl-21'},
            'amazon.co.uk': {'tag': 'afflink-21'}
        }
    '''

    new_url = urlparse(url)
    if not new_url.netloc:
        return None  # rather raise an Exception?

    # Inser domain check below using domain_extract package
    # if new_url.netloc != 'www.amazon.com':
    #     return url

    # make sure this is a product URL. FIXME why is this important, which URLs
    # do not work when tag param is added?
    # if '/dp/' not in new_url.path and '/gp/product/' not in new_url.path:
    #     return url

    # remove original querystring and add affiliate tag
    new_url = new_url[:4] + (
        urlencode({'tag': affiliate_tag}, True), ) + new_url[5:]
    return urlunparse(new_url)
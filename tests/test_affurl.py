#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_affurl
----------------------------------

Tests for `affurl` module.
"""

import unittest

from urlparse import parse_qs, urlsplit

from affurl import affurl


class TestAffurl(unittest.TestCase):

    def assertEquivalentUrls(self, url1, url2):
        # TODO parse urls and compare parts with asserts
        purl1 = urlsplit(url1)
        purl2 = urlsplit(url2)

        self.assertEqual(purl1.scheme, purl2.scheme)
        self.assertEqual(purl1.netloc, purl2.netloc)
        self.assertEqual(purl1.path, purl2.path)
        self.assertEqual(parse_qs(purl1.query), parse_qs(purl2.query))
        self.assertEqual(purl1.fragment, purl2.fragment)

    def setUp(self):
        self.mapping = {
            'amazon.com': {'tag': ['affurl-20']},
            'amazon.de': {'tag': ['affurl-21']},
            'amazon.co.uk': {'tag': ['afflink-21']}
        }

    def test_convert_equivalent(self):
        '''Test that converted URLs are equivalent.

        The order of query parameters in a URL doesn't matter so that two
        different URL strings can point to the same resource, thus test
        equivalence and not equality.'''

        # List of tuples where the 1st item is the URL to convert and the 2nd
        # the expected result.
        urls = [
            # URL that should stay the same
            ('http://example.com/path?q=1', 'http://example.com/path?q=1'),
            # home page
            ('http://www.amazon.com/', 'http://www.amazon.com/?tag=affurl-20'),
            # home page with existing tag in URL
            ('http://www.amazon.com/?tag=XXX',
             'http://www.amazon.com/?tag=affurl-20'),
            # product page
            ('http://www.amazon.com/dp/1906966141?ie=UTF8',
             'http://www.amazon.com/dp/1906966141?ie=UTF8&tag=affurl-20'),
            # best seller page
            ('http://www.amazon.com/Laptops-Tablets/b/ref=nav_shopall_lapnet?ie=UTF8&node=2956501011',
             'http://www.amazon.com/Laptops-Tablets/b/ref=nav_shopall_lapnet?ie=UTF8&node=2956501011&tag=affurl-20'),
            # UK page
            ('http://www.amazon.co.uk/Best-Sellers-Welcome/zgbs/',
             'http://www.amazon.co.uk/Best-Sellers-Welcome/zgbs/?tag=afflink-21'),
        ]

        for url in urls:
            url1 = url[1]  # expected value
            url2 = affurl.convert(url[0], self.mapping)  # converted URL
            self.assertEquivalentUrls(url1, url2)

    def test_convert_not_converted(self):
        '''Test to make sure URL is actually changed.

        Test URLs have only 1 parameter so that order of query dict doesn't
        matter.'''

        # List of tuples where the 1st item is the URL to convert and the 2nd
        # the expected result.
        urls = [
            # home page with existing tag in URL
            ('http://www.amazon.com/?tag=XXX',
             'http://www.amazon.com/?tag=XXX'),
        ]

        for url in urls:
            url1 = url[1]  # expected value
            url2 = affurl.convert(url[0], self.mapping)  # converted URL
            self.assertNotEqual(url1, url2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_affurl
----------------------------------

Tests for `affurl` module.
"""

import unittest

from affurl import affurl


class TestAffurl(unittest.TestCase):

    def setUp(self):
        self.mapping = {
            'amazon.com': {'tag': 'affurl-20'},
            'amazon.de': {'tag': 'affurl-21'},
            'amazon.co.uk': {'tag': 'afflink-21'}
        }

    def test_convert(self):
        # List of tuples where the 1st item is the URL to convert and the 2nd
        # the expected result.
        # FIXME Problem needs to sort URL params for tests to work or another idea!
        urls = [
            # URL that should stay the same
            ('http://example.com/path?q=1', 'http://example.com/path?q=1'),
            # home page
            ('http://www.amazon.com/', 'http://www.amazon.com/?tag=affurl-20'),
            # product page
            ('http://www.amazon.com/Python-Language-Reference-Manual/dp/1906966141/ref=la_B0034OPA4K_1_1?s=books&ie=UTF8&qid=1411728826&sr=1-1',
             'http://www.amazon.com/Python-Language-Reference-Manual/dp/1906966141/ref=la_B0034OPA4K_1_1?s=books&ie=UTF8&qid=1411728826&sr=1-1&tag=affurl-20')
        ]

        for url in urls:
            self.assertEqual(url[1], affurl.convert(url[0], self.mapping))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
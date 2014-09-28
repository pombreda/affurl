# -*- coding: utf-8 -*-
"""
affurl.compat
~~~~~~~~~~~~~
Imports and declarations for Python 2 and Python 3 compatibility.
"""
import sys

is3 = sys.version_info[0] == 3

if is3:
     from urllib.parse import parse_qs, urlsplit, urlunsplit
else:
    from urllib import urlencode
    from urlparse import parse_qs, urlsplit, urlunsplit
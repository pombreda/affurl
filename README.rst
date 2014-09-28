===============================
affurl
===============================

.. image:: https://badge.fury.io/py/affurl.png
    :target: http://badge.fury.io/py/affurl

.. image:: https://travis-ci.org/yaph/affurl.png?branch=master
        :target: https://travis-ci.org/yaph/affurl

.. image:: https://pypip.in/d/affurl/badge.png
        :target: https://pypi.python.org/pypi/affurl

Quickstart
----------

Turn URLs into affiliate URLs based on provided domain parameter mapping. This package currently works provided you only need to add or change query parameters of the URL, an example are links to different Amazon domains. See the code and the result below.

Usage
~~~~~

::

    from affurl import affurl

    mapping = {
        'amazon.com': {'tag': ['affurl-20']},
        'amazon.co.uk': {'tag': ['afflink-21']}
    }
    urls = [
        'http://www.amazon.com/', # no existing URL params
        'http://www.amazon.com/dp/1906966141?ie=UTF8',# with URL params
        'http://www.amazon.com/dp/1906966141?tag=XXX',# replace existing tag
        'http://www.amazon.co.uk/Best-Sellers-Welcome/zgbs/' # different domain and tag
    ]
    for url in urls:
        print(affurl.convert(url, mapping))

Output
~~~~~~

| http://www.amazon.com/?tag=affurl-20
| http://www.amazon.com/dp/1906966141?tag=affurl-20&ie=UTF8
| http://www.amazon.com/dp/1906966141?tag=affurl-20
| http://www.amazon.co.uk/Best-Sellers-Welcome/zgbs/?tag=afflink-21

About
-----

* Free software: MIT license
* Documentation: https://pythonhosted.org/affurl/

TODO
----

* Make it work under Python 2 and 3, to fix:
    * urllib
* Make it possible to replace the host part
========
Usage
========

To use affurl in a project:

.. code:: python

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

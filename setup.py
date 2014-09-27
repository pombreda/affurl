#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
requirements = open('requirements.txt').read().splitlines()

setup(
    name='affurl',
    version='0.1.0',
    description='Turn URLs into affiliate URLs based on provided domain parameter mapping',
    long_description=readme + '\n\n' + history,
    author='Ramiro Gómez',
    author_email='code@ramiro.org',
    url='https://github.com/yaph/affurl',
    packages=[
        'affurl',
    ],
    package_dir={'affurl':
                 'affurl'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='affurl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    # tests_require=test_requirements
)
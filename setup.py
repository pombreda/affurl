#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
#requirements = open('requirements.txt').read().splitlines()

setup(
    name='affurl',
    version='0.1.7',
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
    #install_requires=requirements,
    install_requires=['domain_parser'],
    dependency_links=['git+https://github.com/jeffknupp/domain-parser.git@912f466361b6f89dcdb308b2ff03c99471cf96df#egg=domain_parser-master'],
    license='MIT',
    zip_safe=False,
    keywords='affurl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    # tests_require=test_requirements
)
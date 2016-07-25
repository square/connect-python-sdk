# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "squareconnect"
VERSION = "2.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Square Connect API",
    author_email="",
    url="",
    keywords=["Swagger", "Square Connect API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    
    """
)



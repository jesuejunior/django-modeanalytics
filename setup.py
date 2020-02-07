from codecs import open  # To use a consistent encoding
from os import path

from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

setup(
    name="django-mode",
    version="0.0.1",
    description="Django Mode Analytics Whitelabel",
    long_description="",
    url="https://github.com/jesuejunior/django-mode",
    author="jesue Junior",
    author_email="jesuesousa@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)

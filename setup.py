from codecs import open  # To use a consistent encoding
from os import path

from setuptools import (  # Always prefer setuptools over distutils
    find_packages,
    setup,
)

here = path.abspath(path.dirname(__file__))

setup(
    name="python-boilerplate",
    version="0.0.1",
    description="Python Boilerplate Project",
    long_description="",
    url="https://github.com/daltonmatos/python-boilerplate",
    # Author details
    author="Dalton Matos",
    author_email="daltonmatos@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)

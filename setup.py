from codecs import open  # To use a consistent encoding
from os import path

from setuptools import find_packages, setup  # Always prefer setuptools over distutils

here = path.abspath(path.dirname(__file__))

setup(
    name="modeanalytics",
    version="0.1.1",
    description="Django Mode Analytics Whitelabel",
    long_description=(open("README.md").read()),
    long_description_content_type="text/markdown",
    url="https://github.com/jesuejunior/django-modeanalytics",
    author="jesue Junior",
    author_email="jesuesousa@gmail.com",
    license="BSD-3",
    platforms=["OS Independent"],
    keywords="mode analytics data dashboard bi",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*", "test_app", "test_project"]),
    include_package_data=True,
    test_suite="",
    install_requires=["django", "psycopg2>=2"],
    entry_points={},
    zip_safe=False,
)

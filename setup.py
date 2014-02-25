#!/usr/bin/env python
from setuptools import setup

setup(
    name="setquery",
    version="0.2",
    description="Set arithmetic evaluator",
    author="Paul Scott",
    author_email="paul@duedil.com",
    url="https://github.com/icio/setquery",
    download_url="https://github.com/icio/setquery/tarball/0.2",
    setup_requires=["nose", "rednose"],
    py_modules=["setquery", "test_setquery"],
    license="MIT",
    keywords=['set', 'expression', 'eval', 'evaluate'],
    classifiers=[],
)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-nestjs", # Replace with your own username
    version="0.0.4",
    author="Jerry Wang",
    author_email="wangjianjun@gmail.com",
    description="The library for nest style microservice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jerrywang1981/python-nest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

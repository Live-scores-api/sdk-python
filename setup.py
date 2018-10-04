#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:20:33 2018

@author: shrey.aryan
"""
import setuptools
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def read(filename):
    with open(os.path.join(BASE_DIR, filename)) as file:
        return file.read()

setuptools.setup(
    name="sdk-python",
    version="0.0.1",
    author="SuperMario",
    author_email="email@example.com",
    description='Client-Server SDK for LiveScore',
    long_description=read('README.rst'),
    long_description_content_type="text/markdown",
    url="https://github.com/Livescore-api/sdk-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


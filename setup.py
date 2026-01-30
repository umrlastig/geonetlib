# -*- coding: utf-8 -*-
import os
from setuptools import setup

current_path = os.path.abspath(os.path.dirname(__file__))

requirements = (
        "tracklib"
)

dev_requirements = (
        "pytest",
        "pytest-runner",
        "coverage"
)

setup (
    name="netmatcher",
    version="0.1.0",
    description="netmatcher",
    long_description="See https://github.com/umrlastig/netmatcher",
    url="https://github.com/umrlastig/netmatcher",
    author="Marie-Dominique Van Damme",
    author_email="todo",
    keywords=['NetMatcher', 'Python library', 'Map-matching', 'Network'],
    license="Cecill-C",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
    ],
    packages = ['netmatcher','netmatcher.process','netmatcher.io','netmatcher.util'],
    install_requires=requirements,
    test_suite="tests",
    extras_require={
        "dev": dev_requirements
    },
)

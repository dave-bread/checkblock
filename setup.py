# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='checkblock',
    version='0.1.0',
    description='Mail block check',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/dave-bread/checkblock.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


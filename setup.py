# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

version = "0.1.2"

with open('README.md') as f:
    readme = f.read()

setup(
    name="easybq",
    version=version,
    url='https://github.com/ukwksk/easybq',
    packages=[package for package in find_packages()
              if package.startswith('easybq')],
    description="BigQuery Wrapper",
    long_description=readme,
    keywords="Google BigQuery",
    author='ukwksk',
    author_email='pylibs@ukwksk.co',
    maintainer='ukwksk',
    maintainer_email='pylibs@ukwksk.co',
    python_requires='>=3.6',
    install_requires=[
        'google-cloud-bigquery',
    ],
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
)

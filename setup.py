#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='okam-security',
    version='0.1.1',
    python_requires='>=3.5',
    description='A Python port of the Mako (PHP framework) security library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Frederic G. Østby',
    author_email='frederic.g.ostby@gmail.com',
    url='https://github.com/freost/okam-security',
    packages=[
        'okam.security',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/freost/okam-security/issues',
        'Source Code': 'https://github.com/freost/okam-security',
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False
)

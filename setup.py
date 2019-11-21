#!/usr/bin/env python3

from setuptools import setup

setup(
    name='okam-security',
    version='0.1.0',
    python_requires='>=3.5',
    description='A Python port of the Mako (PHP) framework security library.',
    author='Frederic G. Østby',
    author_email='frederic.g.ostby@gmail.com',
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
        'Programming Language :: Python',
    ],
    zip_safe=False
)

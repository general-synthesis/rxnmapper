#!/usr/bin/env python

import os
from setuptools import setup, find_packages

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = '''Reaction atom-mapping from transfomers'''

setup(
    name='rxnmapper',
    version='0.1.4',
    author='RXNMapper team',
    author_email='',
    py_modules=['rxnmapper'],
    description='Reaction atom-mapping from transfomers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=[
        'transformers', 'torch', 'scipy', 'rdkit-pypi'
    ],
    packages=find_packages(),
    package_data={
        'rxnmapper': ['models/transformers/albert_heads_8_uspto_all_1310k/*']
    },
    url='https://github.com/rxn4chemistry/rxnmapper',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

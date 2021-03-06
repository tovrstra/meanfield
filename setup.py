#!/usr/bin/env python

from __future__ import print_function
import os

import numpy as np
from setuptools import setup, Extension
import Cython.Build

from tools.gitversion import get_gitversion


def get_version():
    """Load the version from version.py, without importing it.
    This function assumes that the last line in the file contains a variable defining the
    version string with single quotes.
    """
    with open('meanfield/version.py', 'r') as f:
        return f.read().split('=')[-1].replace('\'', '').strip()


def get_readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='meanfield',
    version=get_version(),
    description='HORTON module for SCF and HF/DFT methods',
    long_description=get_readme(),
    author='Toon Verstraelen',
    author_email='Toon.Verstraelen@UGent.be',
    url='https://github.com/theochem/meanfield',
    cmdclass={'build_ext': Cython.Build.build_ext},
    package_dir={'meanfield': 'meanfield'},
    packages=['meanfield', 'meanfield.test'],
    ext_modules=[Extension(
        'meanfield.cext',
        sources=['meanfield/cext.pyx'],
        include_dirs=[np.get_include()],
    )],
    zip_safe=False,
    setup_requires=['numpy>=1.0', 'cython>=0.24.1'],
    install_requires=['numpy>=1.0', 'nose>=0.11', 'cython>=0.24.1'],
)

# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name='Starter',
    version='0.0.1',
    provides=['starter'],
    author='sroberts',
    url='https://github.com/sroberts/python-starter',
    setup_requires='setuptools',
    license='Apache License v 2.0',
    author_email='scott.roberts@gmail.com',
    description='A start.',
    packages=find_packages(),
    install_requires=[
        'argparse==1.3.0'
    ],
    entry_points={
        'console_scripts': [
            'starter=starter.starter:main',
        ],
    },
)

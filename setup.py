#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name='enhanced_rds',
    version='0.2.0',
    description='AWS Lambda function wrapper to capture metrics from enhanced RDS monitoring logs',
    zip_safe=True,
    packages=find_packages(),
    install_requires=requirements,
    author='Trevor O\'Connor',
    author_email='trevor@signalfx.com',
    license='Apache Software License v2',
    url='https://github.com/signalfx/enhanced-rds-monitoring'
)
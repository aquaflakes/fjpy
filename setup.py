#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='fjpy',
    url='https://github.com/jladan/package_demo',
    author='Fangjie Zhu',
    # Needed to actually package something
    packages=find_packages(),#['fjpy'],
    # Needed for dependencies
    install_requires=['pipimport','numpy','ggplot','pandas','SciPy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='some utilities',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
    # scripts=['']
)



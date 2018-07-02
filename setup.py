#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages
setup(
     name='fjpy',    # This is the name of your PyPI-package.
     version='1.0',                          # Update the version number for new releases
     description='',
     packages=find_packages(),
     url='https://github.com/aquaflakes/fjpy',
     install_requires=['pipimport','numpy','ggplot','pandas','SciPy'],
     scripts=['']                  # The name of your scipt, and also the command you'll be using for calling it
)

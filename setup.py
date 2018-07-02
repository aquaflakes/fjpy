#!/usr/bin/env python
# from setuptools import setup
# from setuptools import find_packages
# setup(
#      name='fjpy',    # This is the name of your PyPI-package.
#      version='1.0',                          # Update the version number for new releases
#      description='',
#      packages=['fjpy'],#find_packages(),
#      url='https://github.com/aquaflakes/fjpy',
#      install_requires=['pipimport','numpy','ggplot','pandas','SciPy'],
#      scripts=['']                  # The name of your scipt, and also the command you'll be using for calling it
# )

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='fjpy',
    url='https://github.com/jladan/package_demo',
    author='Fangjie Zhu',
    # Needed to actually package something
    packages=['fjpy'],
    # Needed for dependencies
    install_requires=['pipimport','numpy','ggplot','pandas','SciPy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
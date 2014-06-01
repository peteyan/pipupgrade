#!/usr/bin/python
from setuptools import setup, find_packages


setup(name='pipupgrade',
      version='0.1.0',
      author='Jan Zegan',
      description='Check and/or update all Python packages with pip',
      author_email='jzegan@gmail.com',
      #packages=find_packages(),
      install_requires=['pip'],
      py_modules = ['scripts.pipupgrade'],
      entry_points={
          'console_scripts': ['pipupgrade = scripts.pipupgrade:main']
          }
      )

#!/usr/bin/env python

import sys
import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup

setup(name='winreg_unicode',
      version='0.5.0',
      description='a Unicode-aware winreg package for Python 2',
      author='Stutzbach Enterprises, LLC',
      author_email='daniel@stutzbachenterprises.com',
      url='http://stutzbachenterprises.com/',
      license = "BSD",
      keywords = "winreg unicode Windows registry",
      provides = ['winreg_unicode'],
      py_modules = ['winreg_unicode'],
      #test_suite = "test_winreg_unicode",
      zip_safe = True,
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Win32 (MS Windows)',
          'Operating System :: Microsoft :: Windows',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          ],

      long_description=open('README.rst').read(),

      )

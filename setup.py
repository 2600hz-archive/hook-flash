#!/usr/bin/env python

import os.path
from setuptools import setup, find_packages

setup(name='hook-flash',
      version='0.0.1',
      description='A rtmp-sip gateway based on rtmplite and p2psip.',
      author='Ben Wann',
      author_email='ben@2600hz.com',
      url='https://github.com/2600hz/hook-flash',
      install_requires=['multitask','p2psip'],
      packages=['rtmplite'],
      scripts=['rtmplite/siprtmp_gevent.py', 'rtmplite/siprtmp.py'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ])

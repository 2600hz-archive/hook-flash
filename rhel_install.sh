#!/bin/bash
yum -y install python-devel python-pip
pip install cython git+git://github.com/surfly/gevent.git#egg=gevent

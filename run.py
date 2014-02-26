#!/usr/bin/env python
import os, sys, rtmplite, p2psip
from pkg_resources import require
os.system("siprtmp_gevent.py -d -g 192.168.56.110:5060")

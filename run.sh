#!/bin/sh
path=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
script="$path/hook_flash-0.0.1-py2.6.egg/gateway/siprtmp_gevent.py"
python $script  -d -g 127.0.0.1:5060 & 

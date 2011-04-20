#!/usr/bin/python
import Xlib
import Xlib.display
import time
import os
import subprocess

# xsendkeys is in ubuntu package lineakd
subprocess.Popen(['gnome-terminal'])
time.sleep(2)
subprocess.Popen(['xsendkeys','l+s+Return'])
time.sleep(3)
os.system('xsendkeys Alt+F4')

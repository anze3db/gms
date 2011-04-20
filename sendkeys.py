import Xlib
import Xlib.display
import time
import os

# xsendkeys is in ubuntu package lineakd
os.system('gnome-terminal')
time.sleep(1)
os.system('xsendkeys l+s+Return')
time.sleep(3)
os.system('wmctrl -r gnome-terminal -b toggle,hidden')
time.sleep(2)
os.system('wmctrl -a gnome-terminal')
time.sleep(3)
os.system('xsendkeys Alt+F4')

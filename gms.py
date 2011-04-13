'''
Created on Apr 11, 2011

@author: smotko
'''

import Xlib
import Xlib.display
import time
 
def mousepos():
    """mousepos() --> (x, y) get  the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]
 
if __name__ == "__main__":
    
    KEYBOARD = '/dev/input/by-path/platform-i8042-serio-0-event-kbd'
    
    while True:
        scanner_device = open(KEYBOARD,"r")
        # log stuff to file here
        print repr(scanner_device.readline())
        scanner_device.close()
        time.sleep(0.1)
        
    
    #while(True):
        #print("{0}".format(mousepos()))
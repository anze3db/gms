'''
Created on Apr 11, 2011

@author: smotko
'''

from Xlib import display
 
def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]
 
if __name__ == "__main__":
    print("The mouse position on the screen is {0}".format(mousepos()))
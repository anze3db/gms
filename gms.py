'''
Created on Apr 11, 2011

@author: smotko
'''
import Xlib
import Xlib.display
import time
 
def OnKeyDown(event):
    print event

def OnKeyUp(event):
    print event
 
def OnMouseDown(event):
    print event

def OnMoseUp(event):
    print event.MessageName, event.Position, event.Window, event.WindowName, event.WindowProcName

# EVENT: 'MessageName', 'Position', 'Window', 'WindowName', 'WindowProcName'

if __name__ == "__main__":
    
    
    import pyxhook as pimp
    
    hooker = pimp.HookManager()
    
    # Keyboard start hookin':
    hooker.HookKeyboard()
    hooker.KeyDown = OnKeyDown
    hooker.KeyUp = OnKeyUp
    
    # Mouse start hookin':
    hooker.HookMouse()
    hooker.MouseAllButtonsDown = OnMouseDown
    hooker.MouseAllButtonsUp = OnMoseUp
    
    hooker.start()
    
    #KEYBOARD = '/dev/input/by-path/platform-i8042-serio-0-event-kbd'
    
    #while True:
    #    scanner_device = open(KEYBOARD,"r")
    #    # log stuff to file here
    #    print repr(scanner_device.readline())
    #    scanner_device.close()
    #    time.sleep(0.1)
        
    
    #while(True):
        #print("{0}".format(mousepos()))
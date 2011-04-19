#!/usr/bin/python
'''
Created on Apr 11, 2011

@author: smotko
'''
import Xlib
import Xlib.display
import time
import sys
 
def OnKeyDown(event):
    if event.Key == 'x':
        sys.exit()
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
 
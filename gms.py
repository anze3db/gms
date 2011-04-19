#!/usr/bin/python
'''
Created on Apr 11, 2011

@authors: Anze, Matic, Miha
'''
from sys import exit
from Xlib import display

superPressed = False
rightMousePressed = False
 
def OnKeyDown(event):
    if event.Key == 'x':
        exit()
    if event.Key == 'Super_L':
        superPressed = True
    
def OnKeyUp(event):
    if event.Key == 'Super_L':
        superPressed = False
 
def OnMouseDown(event):
    if event.MessageName == 'mouse right down':
        rightMousePressed = True

def OnMoseUp(event):
    if event.MessageName == 'mouse right up':
        rightMousePressed = False

def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

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
 
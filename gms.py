#!/usr/bin/python
'''
Created on Apr 11, 2011

@authors: Anze, Matic, Miha
'''

from sys import exit
from Xlib import display
from thread import start_new_thread

superPressed = False
rightMousePressed = False
frame = False
 
def OnKeyDown(event):
    global superPressed
    if event.Key == 'x':
        exit()
    if event.Key == 'Super_L':
        superPressed = True
        
def OnKeyUp(event):
    global superPressed
    if event.Key == 'Super_L':
        superPressed = False
        
def OnMouseDown(event):
    global rightMousePressed
    global superPressed
    global frame
    
    frame.setClicked(event.WindowName)
    
    if event.MessageName == 'mouse right down':
        rightMousePressed = True
        
        if superPressed:
            start_new_thread(record_mouse_pos, ())
        
def OnMoseUp(event):
    if event.MessageName == 'mouse right up':
        global rightMousePressed
        rightMousePressed = False
        
def record_mouse_pos():
    gesture = []
    global rightMousePressed
    while rightMousePressed:
        gesture.append(mousepos())
    parse_gesture(gesture)

def parse_gesture(coordinates):
    
    global frame
    frame.debug_output.SetValue(str(coordinates))


def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

# EVENT: 'MessageName', 'Position', 'Window', 'WindowName', 'WindowProcName'

def start_gui():
    
    global frame
    
    from gui.GMS import GMS
    import wx
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame = GMS(None, -1, "")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()

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
    
    # start GUI:
    start_new_thread(start_gui, ())
    
 
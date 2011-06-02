#!/usr/bin/python
'''
Created on Apr 11, 2011

@authors: Anze, Matic, Miha
'''
from sys import exit
from Xlib import display
from thread import start_new_thread
from models import settings
superPressed = False
rightMousePressed = False
frame = False

def openSettings():
    from settingsFrame import SettingsFrame
    from wx import App
    app = App(False)
    frame = SettingsFrame(None, 'GMS Settings')
    app.MainLoop()

def OnKeyDown(event):
    global superPressed
        
    if event.Key == settings.get('default_key'):
        superPressed = True
        
def OnKeyUp(event):
    global superPressed
    if event.Key == settings.get('default_key'):
        superPressed = False
        
def OnMouseDown(event):
    global rightMousePressed
    global superPressed
    global frame

    mouse = settings.get('mouse')
    if not mouse:
        mouse = 'middle'

    if event.MessageName == 'mouse ' + mouse + ' down':
        rightMousePressed = True
        
        if settings.get('default_key'):
            if superPressed:
                start_new_thread(record_mouse_pos, ())
        else:
            start_new_thread(record_mouse_pos, ())
        
        
def OnMoseUp(event):
    mouse = settings.get('mouse')
    if not mouse:
        mouse = 'middle'
    if event.MessageName == 'mouse ' + mouse + ' up':
        global rightMousePressed
        rightMousePressed = False
        
def record_mouse_pos():
    gesture = []
    global rightMousePressed
    while rightMousePressed:
        gesture.append(mousepos())
    parse_gesture(gesture)

def find_gesture(gesture):
    
    key = settings.get(gesture)
    if key:
        import os
        os.system('xsendkeys +'+key)

def parse_gesture(coordinates):
    #print coordinates
    sumX = 0
    sumY = 0
    SENSITIVITY = 200
    gX = False
    gY = False
    
    invalid = False
    
    for i in range(1, len(coordinates)-1):
        (x,y) = coordinates[i] 
        (prevX, prevY) = coordinates[i-1]
        sumX += (x-prevX)
        sumY += (y-prevY)
        
        if abs(sumX) < SENSITIVITY and gX:
            invalid = True
        if abs(sumY) < SENSITIVITY and gY:
            invalid = False
        
        if abs(sumX) > SENSITIVITY:
            gX = True
        if abs(sumY) > SENSITIVITY:
            gY = True
        
    if invalid:
        #print 'invalid'
        return
    
    
    gestureX = ''
    gestureY = ''

    if abs(sumX) > SENSITIVITY:
        d = coordinates[0][0] - coordinates[-1][0]
        if d >= 0:
            gestureX = 'left'
        else:
            gestureX = 'right'
    if abs(sumY) > SENSITIVITY:
        d = coordinates[0][1] - coordinates[-1][1]
        if d >= 0:
            gestureY = 'up' 
        else:
            gestureY = 'down'
    
    find_gesture(gestureY + gestureX)
    

def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

# EVENT: 'MessageName', 'Position', 'Window', 'WindowName', 'WindowProcName'

def setup_hookers():
    import pyxhook as hook
    
    h = hook.HookManager()
    
    # Keyboard start hookin':
    h.HookKeyboard()
    h.KeyDown = OnKeyDown
    h.KeyUp = OnKeyUp
    
    # Mouse start hookin':
    h.HookMouse()
    h.MouseAllButtonsDown = OnMouseDown
    h.MouseAllButtonsUp = OnMoseUp
    h.setDaemon(True)
    h.start()
    

if __name__ == "__main__":
    pass
 

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
    
    #elif event.Key == 's':
        #openSettings()
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
    
    #frame.setClicked(event.WindowName)
    
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
        print 'invalid'
        return
    
    
    gestureX = ''
    gestureY = ''
    
    print abs(sumX), abs(sumY)
    
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
    
    print gestureX, gestureY

    # Parse the coordinates:
    # While odmik po X majhen
    
    # Get action for parsed gesture:
    # Execute action:

def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

# EVENT: 'MessageName', 'Position', 'Window', 'WindowName', 'WindowProcName'

def setup_hookers():
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
    hooker.setDaemon(True)
    hooker.start()
    
    

if __name__ == "__main__":
    
    parse_gesture(
                  
                  [(840, 54), (840, 54), (840, 54), (840, 55), (840, 59), (838, 75), (838, 89), (840, 115), (850, 156), (850, 222), (850, 291), (847, 322), (845, 382), (838, 414), (835, 471), (835, 495), (826, 519), (817, 584), (815, 619), (815, 638), (811, 660), (811, 671), (811, 678), (811, 678), (811, 678), (811, 678), (811, 678), (811, 678), (811, 678), (809, 678)]
                  )
    
    
    
    # Show indicator applet
    

    
 
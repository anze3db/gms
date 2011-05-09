#!/usr/bin/env python

# example scribblesimple.py

 # GTK - The GIMP Toolkit
 # Copyright (C) 1995-1997 Peter Mattis, Spencer Kimball and Josh MacDonald
 #
 # This library is free software; you can redistribute it and/or
 # modify it under the terms of the GNU Library General Public
 # License as published by the Free Software Foundation; either
 # version 2 of the License, or (at your option) any later version.
 #
 # This library is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 # Library General Public License for more details.
 #
 # You should have received a copy of the GNU Library General Public
 # License along with this library; if not, write to the
 # Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 # Boston, MA 02111-1307, USA.


import gtk
import GDK

# Backing pixmap for drawing area
pixmap = None

# Create a new backing pixmap of the appropriate size
def configure_event(widget, event):
    global pixmap

    x, y, width, height = widget.get_allocation()
    pixmap = gtk.create_pixmap(widget.get_window(), width, height, -1)
    gtk.draw_rectangle(pixmap, widget.get_style().white_gc,
                       gtk.TRUE, 0, 0, width, height)

    return gtk.TRUE

# Redraw the screen from the backing pixmap
def expose_event(widget, event):
    x , y, width, height = event.area
    widget.draw_pixmap(widget.get_style().fg_gc[gtk.STATE_NORMAL],
                       pixmap, x, y, x, y, width, height)
    return gtk.FALSE

# Draw a rectangle on the screen
def draw_brush(widget, x, y):
    rect = (x - 5, y - 5, 10, 10)
    gtk.draw_rectangle(pixmap, widget.get_style().black_gc, gtk.TRUE,
                       rect[0], rect[1], rect[2], rect[3])
    widget.draw(rect)

def button_press_event(widget, event):
    if event.button == 1 and pixmap != None:
        draw_brush(widget, event.x, event.y)
    return gtk.TRUE

def motion_notify_event(widget, event):
    if event.is_hint:
        x, y, = event.window.pointer
        state = event.window.pointer_state
    else:
        x = event.x
        y = event.y
        state = event.state
    
    if state & GDK.BUTTON1_MASK and pixmap != None:
        draw_brush(widget, x, y)
  
    return gtk.TRUE

def main():
    window = gtk.GtkWindow(gtk.WINDOW_TOPLEVEL)
    window.set_name ("Test Input")

    vbox = gtk.GtkVBox(gtk.FALSE, 0)
    window.add(vbox)
    vbox.show()

    window.connect("destroy", gtk.mainquit)

    # Create the drawing area
    drawing_area = gtk.GtkDrawingArea()
    drawing_area.size(200, 200)
    vbox.pack_start(drawing_area, gtk.TRUE, gtk.TRUE, 0)

    drawing_area.show()

    # Signals used to handle backing pixmap
    drawing_area.connect("expose_event", expose_event)
    drawing_area.connect("configure_event", configure_event)

    # Event signals
    drawing_area.connect("motion_notify_event", motion_notify_event)
    drawing_area.connect("button_press_event", button_press_event)

    drawing_area.set_events(GDK.EXPOSURE_MASK
                            | GDK.LEAVE_NOTIFY_MASK
                            | GDK.BUTTON_PRESS_MASK
                            | GDK.POINTER_MOTION_MASK
                            | GDK.POINTER_MOTION_HINT_MASK)

    # .. And a quit button
    button = gtk.GtkButton("Quit")
    vbox.pack_start(button, gtk.FALSE, gtk.FALSE, 0)

    button.connect_object("clicked", window.destroy, window)
    button.show()

    window.show()

    gtk.mainloop()

    return 0

if __name__ == "__main__":
    main()


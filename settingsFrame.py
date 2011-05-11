#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from models import settings

class SettingsFrame(gtk.Window):
    
    TITLE = "GMS Settings"
    
    def __init__(self):
        super(SettingsFrame, self).__init__()
        
        self.set_title(self.TITLE)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)
        
        # Set icons on buttons
        #settings = gtk.settings_get_default()
        #settings.props.gtk_button_images = True
        
        hbox1 = gtk.HBox(False, 0)
        hbox2 = gtk.HBox(False, 10)
        hbox3 = gtk.HBox(False, 10)
        vbox = gtk.VBox(False, 3)
        
        valign = gtk.Alignment(0, 1, 0, 0)
        vbox.pack_start(valign)

        label = gtk.Label("Set default key")
        self.set = gtk.Button(settings.get("default_key"))
        self.set.connect("clicked", self.on_set)
        

        hbox2.add(label)
        hbox2.add(self.set)
        halign = gtk.Alignment(0, 1, 0, 0)
        
        halign.add(hbox2)
        vbox.pack_start(halign, False, False, 3)
        
        
        configGestures = gtk.Button("Config Gestures")
        configGestures.connect('clicked', self.on_config_gestures)
        hbox3.add(configGestures)
        halign1 = gtk.Alignment(1, 0, 0, 0)
        
        halign1.add(hbox3)
        
        vbox.pack_start(halign1, False, False, 3)
        
        
        ok = gtk.Button(stock=gtk.STOCK_CLOSE)
        ok.connect("clicked", self.on_close)
        
        hbox1.add(ok)
        halign = gtk.Alignment(1, 0, 0, 0)
        
        halign.add(hbox1)
        vbox.pack_start(halign, False, False, 3)

        
        self.add(vbox)
        
        self.connect("destroy", self.on_close)
        self.show_all()

    def on_config_gestures(self):
        

    def on_set(self, widget):
        
        self.mody = gtk.Window()
        self.mody.set_modal(True)
        self.mody.set_title("Grab")
        self.mody.set_position(gtk.WIN_POS_CENTER_ON_PARENT)
        self.mody.set_border_width(20)
        self.mody.add_events(gtk.gdk.KEY_PRESS)
        self.mody.connect("key_press_event", self.on_grab)
        
        
        
        label = gtk.Label("Press a key...")
        self.mody.add(label)
        self.mody.show_all()
        
    def on_grab(self, widget, event):
        
        self.mody.hide_all()
        print event.keyval
        
        if event.keyval == 65513:
            key = "Alt_L"
        elif event.keyval == 65515:
            key = "Super_L"
        elif event.keyval == 65507:
            key = "Control_L"
        elif event.keyval == 65505:
            key = "Shift_L"
        else:
            return
         
        self.set.set_label(key)
        settings.set('default_key', key)
        
    def on_close(self,widget):
        self.hide_all()
    
    def main(self):
        gtk.main()
          
 
if __name__ == '__main__': 
    frame = SettingsFrame()
    frame.main()

#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from models import settings

class settingsGmsFrame(gtk.Window):
    
    TITLE = "GMS Settings"
    
    def __init__(self):
        super(settingsGmsFrame, self).__init__()
        
        self.set_title(self.TITLE)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)
        self.set_resizable(False)
        
        # Set icons on buttons
        #settings = gtk.settings_get_default()
        #settings.props.gtk_button_images = True
        
        vbox = gtk.VBox(False, 10)



        self.COMBINATIONS = ['left', 'right', 'up', 'down', 
                        'up-left', 'up-right', 'down-left', 'down-right' 
                       ]
        self.table = gtk.Table(2, 2, False)
        self.table.set_col_spacings(10)
        for i,c in enumerate(self.COMBINATIONS):
            label = gtk.Label(c.capitalize())
            label.set_alignment(1,0.5)
            self.table.attach(label, 0,1,i,i+1)
            
            entry = gtk.Entry()
            key = settings.get(c.replace('-', ''))
            entry.set_name(c)
            if key:
                entry.set_text(key)
            self.table.attach(entry, 1,2, i, i+1)
        
        vbox.pack_start_defaults(self.table)
        close = gtk.Button(stock=gtk.STOCK_CLOSE)
        close.connect('clicked', self.on_close)
        align = gtk.Alignment(xalign=1.0, yalign=0.5)
        align.add(close)
        vbox.pack_end_defaults(align)
        
        #self.add(table)
        
        #vbox.pack_end(table, True, True, 0)
        self.add(vbox)
        #self.down = gtk.Entry()
        #self.down.set_text(settings.get('down'))
        
        self.connect("destroy", self.on_close)
        self.show_all()

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
        #print event.keyval
        
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
        #print self.down.get_text()
        
        for child in self.table.get_children():
            
            if child.get_name() in self.COMBINATIONS:
                
                settings.set(child.get_name().replace('-', ''), child.get_text())
                #print "downright anyoine?", child.get_name().replace('-', ''), child.get_text()
                
        self.hide_all()
    
    def main(self):
        gtk.main()
          
 
if __name__ == '__main__': 
    frame = settingsGmsFrame()
    frame.main()

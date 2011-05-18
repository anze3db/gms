#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from models import settings





class SettingsFrame(gtk.Window):
    
    TITLE = "GMS Settings"
    MOUSE = ['left', 'middle', 'right']
    
    def __init__(self):
        super(SettingsFrame, self).__init__()
        
        self.set_title(self.TITLE)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)
        self.set_resizable(False)
        # Set icons on buttons
        #settings = gtk.settings_get_default()
        #settings.props.gtk_button_images = True
        
        #hbox1 = gtk.HBox(False, 0)
        #hbox2 = gtk.HBox(False, 10)
        #hbox3 = gtk.HBox(False, 10)
        vbox = gtk.VBox(False, 10)
        
        #valign = gtk.Alignment(0, 1, 0, 0)
        #vbox.pack_start(valign)
        
        
        
        self.table = gtk.Table(4, 4, False)
        self.table.set_col_spacings(10)
              
        label = gtk.Label("Set default key:")
        label.set_alignment(1,0.5)
        self.set = gtk.Button(str(settings.get("default_key")))
        self.set.connect("clicked", self.on_set)
        clear = gtk.Button("Clear")
        clear.connect('clicked', self.on_clear)
        self.table.attach(clear, 2,3, 1,2)
        
        self.table.attach(label, 0, 1, 1, 2)
        self.table.attach(self.set, 1, 2, 1, 2)
        
        self.table.attach(gtk.Label("Set mouse button:"), 0,1,2,3)
        selectMouse = gtk.combo_box_new_text()
        selectMouse.append_text("Left")
        selectMouse.append_text("Middle")
        selectMouse.append_text("Right")
        selectMouse.connect('changed', self.on_changed_cb)
        
        mouse = settings.get('mouse')
        if mouse:
            selectMouse.set_active(self.MOUSE.index(mouse))
        
        self.table.attach(selectMouse,1,2,2,3)
        
        configGestures = gtk.Button("Config Gestures")
        configGestures.connect('clicked', self.on_config_gestures)
        cf = gtk.Label("Config gestures:")
        cf.set_alignment(1,0.5)
        self.table.attach(cf, 0,1,4,5)
        self.table.attach(configGestures, 1,2,4,5)
        
        
        close = gtk.Button(stock=gtk.STOCK_CLOSE)
        close.connect('clicked', self.on_close)
        align = gtk.Alignment(xalign=1.0, yalign=0.5)
        align.add(close)
        vbox.pack_end_defaults(align)
        
        vbox.pack_start_defaults(self.table)
        vbox.pack_end_defaults(align)
        
        halign = gtk.Alignment(0, 1, 0, 0)
                
        self.add(vbox)
        
        
        self.connect("destroy", self.on_close)
        self.show_all()

    def on_config_gestures(self, widget):
        from configGms import settingsGmsFrame
        settingsGmsFrame()

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
        
    def on_changed_cb(self, widget):
        settings.set('mouse', self.MOUSE[widget.get_active()])
        
    def on_clear(self, widget):
        settings.set('default_key', '')
        self.set.set_label('False')
        #settings.set('mouse', self.MOUSE[widget.get_active()])
          
    
    def main(self):
        gtk.main()
    
 
if __name__ == '__main__': 
    frame = SettingsFrame()
    frame.main()

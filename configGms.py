#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
from models import settings, gestures
from pprint import pprint

class settingsGmsFrame(gtk.Window):
    
    TITLE = "Bind keys"
    
    def __init__(self):
        super(settingsGmsFrame, self).__init__()
        self.no_saving = True
        self.set_title(self.TITLE)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(10)
        self.set_resizable(False)
        
        # Set icons on buttons
        #settings = gtk.settings_get_default()
        #settings.props.gtk_button_images = True
        
        vbox = gtk.VBox(False, 10)
        hbox = gtk.HBox(False, 10)
        
        


        self.COMBINATIONS = ['left', 'right', 'up', 'down', 
                        'up-left', 'up-right', 'down-left', 'down-right' 
                       ]
                       
        frame = gtk.Frame("Global settings")  
        self.table = gtk.Table(2, 2, False)
        self.table.set_col_spacings(10)
        self.table.set_border_width(10)  
        for i,c in enumerate(self.COMBINATIONS):
            label = gtk.Label(c.capitalize())
            label.set_alignment(1,0.5)
            self.table.attach(label, 0,1,i,i+1)
            
            entry = gtk.Entry()
            key = settings.get(c.replace('-', ''))
            entry.set_name(c)
            if key:
                entry.set_text(key)
            entry.connect('changed', self.on_global_changed)
            self.table.attach(entry, 1,2, i, i+1)
            
        frame.add(self.table)        
        
        frame_local = gtk.Frame("Application specific settings")
        
        self.table2 = gtk.Table(2, 2, False)
        self.table2.set_col_spacings(10)
        self.table2.set_border_width(10) 
        label = gtk.Label("Choose a program:")
        label.set_alignment(1,0.5)
        self.select_program = gtk.combo_box_new_text()
        self.select_program.connect('changed', self.on_select_change)
        self.refresh_app_list()
        
        self.add_text = gtk.Entry()
        
        add_label = gtk.Label("Add a new app")
        
        add_button = gtk.Button("Add")
        add_button.connect('clicked', self.on_add_app)
        
        self.remove_button = gtk.Button("Remove")
        self.remove_button.set_sensitive(False)
        self.remove_button.connect('clicked', self.on_remove_app)
        
        self.table2.attach(add_label, 0,1,0,1)
        self.table2.attach(self.add_text, 1,2,0,1)
        self.table2.attach(add_button, 2,3, 0,1)
        self.table2.attach(self.remove_button, 2,3,1,2)
        self.table2.attach(label, 0,1,1,2)
        self.table2.attach(self.select_program, 1,2,1,2)
        
        for i,c in enumerate(self.COMBINATIONS):
            label = gtk.Label(c.capitalize())
            label.set_alignment(1,0.5)
            self.table2.attach(label, 0,1,i+2,i+3)
            
            entry = gtk.Entry()
            entry.connect('changed', self.on_specific_changed)
            
            entry.set_name(c)
            
            self.table2.attach(entry, 1,2, i+2, i+3)
        frame_local.add(self.table2)
        hbox.pack_start_defaults(frame)
        hbox.pack_start_defaults(frame_local)
        vbox.pack_start_defaults(hbox)
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
    def on_global_changed(self, widget):
        settings.set(widget.get_name().replace('-', ''), widget.get_text()) 
    def on_specific_changed(self, widget):
        if self.no_saving:
            return
        model = self.select_program.get_model()
        active = self.select_program.get_active()
        if active < 0:
            return
        # print "saving", model[active][0], widget.get_name(), widget.get_text()
        gestures.add_gesture(model[active][0], widget.get_name(), widget.get_text())
        
    def on_select_change(self, widget):
        self.no_saving = True
        if self.select_program.get_active() < 0:
            self.remove_button.set_sensitive(False)
        else:
            self.remove_button.set_sensitive(True)
        self.refresh_app_inputs()
        self.no_saving = False
            
    def refresh_app_inputs(self):
        active = self.select_program.get_active() 
        if active >= 0:
            model = self.select_program.get_model()
            name = model[active][0]
            arr = gestures.get_app_gestures(name)
            for child in self.table2.get_children():
                if type(child) != type(gtk.Entry()):
                    continue
                was_set = False
                for a in arr:
                    if child.get_name() == a[1]:
                        was_set = True
                        child.set_text(a[2])
                if not was_set:
                    child.set_text("")
        
    def on_remove_app(self, widget):
        model = self.select_program.get_model()
        active = self.select_program.get_active()
        if active < 0:
            return
        gestures.remove_app(model[active][0])
        self.select_program.remove_text(active)
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
        
    def on_add_app(self, widget):        
        gestures.add_app(self.add_text.get_text())
        self.select_program.append_text(self.add_text.get_text())
        self.select_program.set_active(len(self.select_program.get_model())-1)
        self.add_text.set_text("")
        
    def refresh_app_list(self):
        #self.select_program.set_model(None)
        for p in gestures.get_apps():
            self.select_program.append_text(p[1])
        
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

                #print "downright anyoine?", child.get_name().replace('-', ''), child.get_text()
                
        self.hide_all()
    
    def main(self):
        gtk.main()
          
 
if __name__ == '__main__': 
    frame = settingsGmsFrame()
    frame.main()

#!/usr/bin/python
import pygtk
pygtk.require("2.0")

import gtk
import appindicator

from threading import Thread

class AppIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator("Ubuntu Mouse Gestures", "system-file-manager-panel", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        # self.ind.set_attention_icon ("indicator-messages-new")



        # create a menu
        self.menu = gtk.Menu()

        # create items for the menu - labels, checkboxes, radio buttons and images are supported:
        
        title = gtk.MenuItem("Linux Mouse Gestures")
        title.show()
        title.set_sensitive(False)
        self.menu.append(title)
        
        settings = gtk.ImageMenuItem(gtk.STOCK_PREFERENCES)
        settings.show()
        settings.connect("activate", self.settings)
        self.menu.append(settings)

        about = gtk.ImageMenuItem(gtk.STOCK_ABOUT)
        about.connect("activate", self.about)
        about.show()
        self.menu.append(about)

        quit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        quit.connect("activate", self.quit)
        quit.show()
        self.menu.append(quit)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)
        
        self.bg = Thread(target=self.start_log)
        self.bg.start()

    def quit(self, widget, data=None):
        gtk.main_quit()
        
    def settings(self, widget, data=None):
        
        from settingsFrame import SettingsFrame
        
        SettingsFrame()
        
    def about(self, widget):
        
        about = gtk.AboutDialog()
        about.set_version('0.4')
        about.set_name('Linux Mouse Gestures')
        about.set_comments('Super simple and easy mouse gestures in Linux')
        about.set_website('http://psywerx.net')
        about.set_authors(['Anze', 'Matic', 'Miha'])
        about.run()
        about.hide_all()
        
        
    def settings_start(self):
        from settingsFrame import SettingsFrame
        from wx import App
        app = App(False)
        frame = SettingsFrame(None, 'GMS Settings')
        app.MainLoop()
        
        
    def start_log(self):
        from gms import setup_hookers
        
        setup_hookers()
        
    def main(self):
        """
            This function starts GTK drawing the GUI and responding to events
            like button clicks
        """
 
        gtk.main()


def main():
    
    return 0

if __name__ == "__main__":
    indicator = AppIndicator()
    gtk.gdk.threads_init()
    gtk.gdk.threads_enter()
    indicator.main()    
    gtk.gdk.threads_leave()


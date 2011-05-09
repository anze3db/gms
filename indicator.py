#!/usr/bin/python
import pygtk
import gtk
import appindicator

class AppIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator ("example-simple-client", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon ("indicator-messages-new")
        self.ind.set_icon("distributor-logo")

        # create a menu
        self.menu = gtk.Menu()

        # create items for the menu - labels, checkboxes, radio buttons and images are supported:
        
        settings = gtk.MenuItem("Settings")
        settings.show()
        settings.connect("activate", self.settings)
        self.menu.append(settings)

        quit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        quit.connect("activate", self.quit)
        quit.show()
        self.menu.append(quit)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)

    def quit(self, widget, data=None):
        gtk.main_quit()
        
    def settings(self, widget, data=None):
        from settingsFrame import SettingsFrame
        from wx import App
        app = App(False)
        frame = SettingsFrame(None, 'GMS Settings')
        app.MainLoop()

def main():
    gtk.main()
    
    return 0

if __name__ == "__main__":
    indicator = AppIndicator()
    main()

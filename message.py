#!/usr/bin/env python
try:
    import gtk, pygtk, os, os.path, pynotify, sys
    pygtk.require('2.0')
except:
    print "Error: need python-notify, python-gtk2 and gtk"

if __name__ == '__main__':
    if not pynotify.init("Timekpr notification"):
        sys.exit(1)

    n = pynotify.Notification("Download Finished", "aaa", "/usr/share/app-install/icons/deluge.png")
    n.set_urgency(pynotify.URGENCY_CRITICAL)
    n.set_timeout(10000) # 10 seconds
    n.set_category("device")

    #Call an icon
    helper = gtk.Button()
    icon = helper.render_icon(gtk.STOCK_DIALOG_WARNING, gtk.ICON_SIZE_DIALOG)
    n.set_icon_from_pixbuf(icon)

    if not n.show():
        print "Failed to send notification"
        sys.exit(1)

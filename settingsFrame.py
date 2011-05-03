#!/usr/bin/env python

import wx
class SettingsFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,-1))
                
        #Status bar:
        # self.CreateStatusBar()
        
        self.panel = wx.Panel(self,-1)
        from models import settings

        self.btnKey = wx.Button(self.panel, -1, str(settings.get('default_key')) )    
        
        self.sizerHor = wx.BoxSizer(wx.HORIZONTAL)
        
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.btnKey, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(self.sizer)

        self.Bind(wx.EVT_BUTTON, self.OnSetKey, self.btnKey)
        
        #Menu:
        self._menuBar()
        self.Centre()
        self.Show(True)
    
    def _menuBar(self):
        file = wx.Menu()
        
        itemExit = file.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        
        about = wx.Menu()
        itemAbout = about.Append(wx.ID_ABOUT, "&About", "About this application")
        
        menuBar = wx.MenuBar()
        menuBar.Append(file, "&File")
        menuBar.Append(about, "&About")
        
        # Set events:
        self.Bind(wx.EVT_MENU, self.OnAbout, itemAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, itemExit)
        self.SetMenuBar(menuBar)
    
    def OnSetKey(self,e):
        my = GrabKeyFrame(self, "Grab a key")
        my.ShowModal()
        
        
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Mouse Gestures for Linux. By Anze, Miha, Matic.", "About GMS", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self, e):
        self.Close(True)  # Close the frame.
        
    def OnOpen(self, e): 
        dlg = wx.FileDialog(self, "Choose", '', "", "*.*", wx.OPEN)
        dlg.ShowModal()
        
    def OnKeySelect(self, key):
        
        from models import settings
        print settings.get('default_key')
        settings.set('default_key', str(key))
        print settings.get('default_key')
        self.btnKey.SetLabel(str(key))
        
        
class GrabKeyFrame(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, title=title, size=(400,200))
        
        
        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        panel.SetFocus()
        
        self.lblKey = wx.StaticText(panel, -1, "Please press a key")
        
        panel.Bind(wx.EVT_MOVE, self.OnKeyDown)
        self.SetFocus()
        self.Centre()
        self.Show(True)
        
        
    def OnKeyDown(self, e):
        
        # TODO: Figure out why alt and super are both returning 307
        
        if e.GetKeyCode() == 307:
            key = "<super>"
        elif e.GetKeyCode() == 308:
            key = "<ctrl>"
        elif e.GetKeyCode() == 306:
            key = "<shift>"
        else:
            self.lblKey.SetLabel("You can only bind <shift>, <ctrl>, <super>, <alt>")
            return 
        
        self.Parent.OnKeySelect(key)
        self.Close()
 
if __name__ == '__main__': 
    app = wx.App(False)
    frame = SettingsFrame(None, 'GMS Settings')
    app.MainLoop()

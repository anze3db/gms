#!/usr/bin/env python

import wx
class SettingsFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,-1))
                
        #Status bar:
        # self.CreateStatusBar()
        
        self.panel = wx.Panel(self,-1)
        from models import settings
        settings.set('default_key', '<super>')
        self.btnKey = wx.Button(self.panel, -1, "Current GMS &key is " + str(settings.get('default_key')) )    
        
        self.sizerHor = wx.BoxSizer(wx.HORIZONTAL)
        
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.btnKey, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(self.sizer)

                
        #Menu:
        self._menuBar()
        
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

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "Mouse Gestures for Linux. By Anze, Miha, Matic.", "About GMS", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self, e):
        self.Close(True)  # Close the frame.
        
    def OnOpen(self, e): 
        dlg = wx.FileDialog(self, "Choose", '', "", "*.*", wx.OPEN)
        dlg.ShowModal()
 
app = wx.App(False)
frame = SettingsFrame(None, 'GMS Settings')
app.MainLoop()

#!/usr/bin/env python

import wx
class SettingsFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,200))
                
        #Status bar:
        # self.CreateStatusBar()
        
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
frame = SettingsFrame(None, 'Small editor')
app.MainLoop()

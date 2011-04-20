#!/usr/bin/python

import wx
from gui.GMS import GMS

app = wx.PySimpleApp(0)
wx.InitAllImageHandlers()
frame = GMS(None, -1, "")
app.SetTopWindow(frame)
frame.Show()
app.MainLoop()

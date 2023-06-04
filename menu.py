"""
Creando el menú para la aplicación. Por el momento va a contener un solo item de salida
"""

import wx

class miMenu(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        self.InitUI()

    def InitUI(self):
        menu_salir = wx.Menu()
        item_salir = wx.MenuItem(menu_salir, wx.ID_EXIT, "&Salir\tCtrl+s")
        self.Bind(wx.EVT_MENU, self.salir, item_salir)
        menu_salir.Append(item_salir)
        self.Append(menu_salir, "&Menú de opciones")

    def salir(self, event):
        wx.GetApp().ExitMainLoop()
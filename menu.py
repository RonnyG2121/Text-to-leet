"""
Creando el menú para la aplicación. Por el momento va a contener un solo item de salida
"""

import wx

class miMenu(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self)
        self.SetSize((300, 250))
        self.Show(True)
        self.InitUI()

    def InitUI(self):

        barra_menu = wx.MenuBar()
        menu_salir = wx.Menu()
        item_salir = wx.MenuItem(menu_salir, wx.ID_EXIT, "&Salir\tCtrl+s")
        menu_salir.Append(item_salir)
        self.Append(menu_salir, "&Menú de opciones")



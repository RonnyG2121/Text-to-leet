"""
Esta es una aplicación gráfica capaz de usar el módulo conversor para convertir texto natural a leet
"""

import wx
from menu import miMenu

class AppLeet(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        self.InitUI()
        self.SetTitle("Texto a Leet")
        self.SetSize((400, 600))
        mi_menu = miMenu()
        self.SetMenuBar(mi_menu)
        self.Show(True)

    def InitUI(self):
        panel = wx.Panel(self)
        caja1 = wx.BoxSizer(wx.HORIZONTAL)
        lb_ingresar = wx.StaticText(panel, wx.ID_ANY, label="&Ingrese el texto natural\tAlt+e")
        self._tb_ingresar = wx.TextCtrl(panel, wx.ID_EDIT, style=wx.TE_CENTRE | wx.TE_MULTILINE)
        self._tb_ingresar.SetFocus()
        self._btn_convertir = wx.Button(panel, wx.ID_CONVERT, label="&Convertir\tAlt+C")
        lb_resultado = wx.StaticText(panel, wx.ID_ANY, label="&Resultado\tAlt+r")
        self._tb_resultado = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_CENTRE | wx.TE_READONLY)
        self._btn_copy = wx.Button(panel, wx.ID_COPY, label="&Copiar al portapapeles\tCtrl+Alt+c")
        caja1.Add(lb_ingresar, 0, wx.ALL, 5)
        caja1.Add(self._tb_ingresar, 1, wx.EXPAND | wx.ALL, 5)
        caja1.Add(self._btn_convertir, 0, wx.ALL, 5)
        caja1.Add(lb_resultado, 0, wx.ALL, 5)
        caja1.Add(self._tb_resultado, 0, wx.EXPAND | wx.ALL, 5)
        caja1.Add(self._btn_copy, 0, wx.ALL, 5)
        panel.SetSizer(caja1)
        panel.Fit()
        panel.Layout()

# Zona de eventos


if __name__ == "__main__":
    app = wx.App()
    AppLeet(None)
    app.MainLoop()


import wx

class InfoPanel(wx.Panel):
    def __init__(self, parent, id):
        super(InfoPanel, self).__init__(parent, id)
        #wx.Panel.__init__(self, parent, id)

        # place the contral text for displaying the content.
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.TXResult = wx.TextCtrl(self, -1, '', style=wx.TE_MULTILINE|wx.TE_RICH2)
        vbox.Add(self.TXResult, 1, wx.EXPAND)
        self.SetSizer(vbox)
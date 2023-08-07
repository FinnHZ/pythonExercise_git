import wx
from panel.Infopanel import InfoPanel


class PanelSet(wx.Notebook):
    def __init__(self, parent, id):
        wx.Notebook.__init__(self, parent, id)

        self.panels = []    # 建立多个页面的集合list
        self.textPanel = InfoPanel(self, -1)  #提取 info 板块
        self.panels.append(self.textPanel)   # 在 多页面 集合中，添加info板块作为其中一页
        self.AddPage(self.panels[0], u"Information")   # 确定多页面集合中 infopanel 页面的设置，并添加页面名字

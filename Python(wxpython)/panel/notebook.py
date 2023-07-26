# -*- coding: utf-8 -*-
  

  # 其实这个notebook 的模块，功能并非单纯的 记事本， 而是多模块集合 整合地， 其他具体功能的模块，写好之后
      # 都放到这个py里 去提取->作为页面添加到主版块->确定页面设置并赋名

import wx
from panel.TestPanel import MyPanel
from panel.TextPanel import TXPanel

class FXNoteBook(wx.Notebook):
    def __init__(self, parent, id):
        wx.Notebook.__init__(self, parent, id)
        self.panels = []    # 建立多个页面的集合list

        self.testPanel = MyPanel(self, -1)  #提取 计算器 板块
        self.textPanel = TXPanel(self, -1)
        self.panels.append(self.testPanel)   # 在 多页面 集合中，添加计算器板块作为其中一页
        self.panels.append(self.textPanel)
        self.AddPage(self.panels[0], u"calculator")   # 确定多页面集合中 计算器 页面的设置，并添加页面名字
        self.AddPage(self.panels[1], u"text")
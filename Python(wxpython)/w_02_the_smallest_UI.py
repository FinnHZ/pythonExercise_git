import wx

#!/user/bin/env python           #this sentence is used by Linux

from wx.core import Frame



class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的 __init__, 否则OnInit方法不会被调用
        #wx.App.__init__(self)         #this sentence has the same features with the next sentence.
        super(self.__class__, self).__init__()
        
    
    def OnInit(self):
        self.version = u"the second course"
        self.title =u"wxpython basic course --" + self.version
        frame = MainFrame(None, -1, self.title)    # -1 --> random id 
        frame.Show(True)
        
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
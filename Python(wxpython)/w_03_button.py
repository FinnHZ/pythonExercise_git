#!/user/bin/env python           #this sentence is used by Linux
import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (500,300))

        # display button features
        self.buttonOK = wx.Button(self, -1, u"OK", (20,20),(60,30))  # (20,20) is the location of the button . (60,30) is the size of the button.
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.buttonOK)   # 把 EVT_BUTTON 通过  self.OnClick 这个函数 绑定（bind）到  self.buttonOK 这个按钮上

        self.buttonCancel = wx.Button(self, -1, u"Cancel", (20,80),(60,30))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.buttonCancel)



    # the features of button 
    def OnClick(self, event):
        if event.GetEventObject() == self.buttonOK:
            print ('{}'.format(event.GetEventObject().GetLabel()))  # get the label(u"OK") of the event object(self.buttonOK)
        elif event.GetEventObject() == self.buttonCancel:
            print ('{}'.format(event.GetEventObject().GetLabel()))
        else:
            print("No button is clicked")

class App(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的 __init__, 否则OnInit方法不会被调用
        #wx.App.__init__(self)         #this sentence has the same features with the next sentence.
        super(self.__class__, self).__init__()
        
    
    def OnInit(self):
        self.version = u"the second course"
        self.title =u"wxpython basic course --" + self.version
        frame = MainFrame(None, -1, self.title)
        frame.Show(True)
        
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
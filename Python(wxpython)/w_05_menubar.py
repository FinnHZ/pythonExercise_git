#!/user/bin/env python           #this sentence is used by Linux
import wx
import time



from wx.core import ID_ABOUT, ID_EXIT, version

Version = "0.1"
ReleaseDate = "14/07/2021"

ID_EXIT = 200
ID_ABOUT = 201
ID_MR = 100

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (500,300))
         # create state bar
        self.setupStatusBar()
        # display button features
        self.initUI()
        # create menu bar
        self.setupMenuBar()
        

    def setupMenuBar(self):
        """create menu baru"""
        #create main men
        menubar = wx.MenuBar()
         # children menu (Quit)
        fmenu = wx.Menu()    #  此时开始设置的就是 菜单栏中，fmenu 的属性，以及它下面 子菜单的 属性， 直到菜单栏中的另一个一级菜单项目（hmenu）开始设置为止
        fmenu.Append(ID_EXIT, u'QUIT(&Q)', 'Terminate the program')  #在 fmenu 这个以及菜单item 下 直接添加id为ID_EXIT的 quit 子菜单
         # add children menu'Quit' into item(File) of main menu
        menubar.Append(fmenu, u'File(&S)')        # 如果没有特别声明，默认快捷键为 Alt + 对应名字的首字母键，自动添加快捷键，如果‘&字母’的形式在括号内声明，则快捷键以声明的为准
        hmenu = wx.Menu()
         # add children menu'ABOUT' into item(HELP) of main menu
        hmenu.Append(ID_ABOUT, u'ABOUT(&A)', 'More information about this program')
        menubar.Append(hmenu, u'HELP(&H)')

        self.SetMenuBar(menubar)   #!! add the whole menu block into our Frame.
        # bind the action for the children menu of the main menu
        wx.EVT_MENU(self, ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        wx.EVT_CLOSE(self, self.OnCloseWindow)


    def initUI(self):
        """display button features"""
        self.buttonOK = wx.Button(self, -1, u"OK", (20,20),(60,30))  # (20,20) is the location of the button . (60,30) is the size of the button.
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.buttonOK)   # 把 EVT_BUTTON 通过  self.OnClick 这个函数 绑定（bind）到  self.buttonOK 这个按钮上

        self.buttonCancel = wx.Button(self, -1, u"Cancel", (20,80),(60,30))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.buttonCancel)


    def OnClick(self, event):
        if event.GetEventObject() == self.buttonOK:
            print ('{}'.format(event.GetEventObject().GetLabel()))  # get the label(u"OK") of the event object(self.buttonOK)
        elif event.GetEventObject() == self.buttonCancel:
            print ('{}'.format(event.GetEventObject().GetLabel()))
        else:
            print("No button is clicked")


    def setupStatusBar(self):
        """create state bar"""
        sb =  self.CreateStatusBar(2)      # create status of window
        self.SetStatusWidths([-1,-2])      # the status is divdided into two parts, the ratio of two is 1:2
        self.SetStatusText("Ready",0)      # 0 represent the first position of the status

        #timer
        self.timer = wx.PyTimer(self.Notify)  # derived from wx.Timer
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)     # 1000 means we begin with 1 second, and TIMER_CONTINUOUS can keep it always run....
        self.Notify()


    def Notify(self):
        t = time.localtime(time.time())   # t 将会以时间戳的形式被赋值
        st = time.strftime('%d/%m/%Y %H:%M:%S', t)  # 将 t 的时间戳转化为正常时间格式
        self.SetStatusText(st, 1)   #将这个时间 显示在 status 的第二个位置上。

    def OnMenuExit(self, event):
        self.Close()
    
    def OnMenuAbout(self, event):
        dlg = AboutDialog(None, -1)
        dlg.ShowModal()
        dlg.Destroy()

    def OnCloseWindow(self, event):
        self.Destroy()

# define a dialog box

class AboutDialog(wx.Dialog):
    def __init__(self, parent, id):
       wx.Dialog.__init__(self, parent, id, "About Me", size = (200,200))

       self.sizerl = wx.BoxSizer(wx.VERTICAL)  # wx.VERTICAL的意思是将下面添加的内容，在wx这个box里面 自上而下，垂直排列。
       self.sizerl.Add(wx.StaticText(self, -1, u"wxpython basic course"), 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, border=20)
       self.sizerl.Add(wx.StaticText(self, -1, u"(c) asdsadddddddww"), 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, border=10)
       self.sizerl.Add(wx.StaticText(self, -1, "Version %s, %s" % (Version, ReleaseDate)), 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, border=10)
       self.sizerl.Add(wx.StaticText(self, -1, u"Autor : Mr Fan"), 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, border=10)
       self.sizerl.Add(wx.Button(self, wx.ID_OK), 0, wx.ALIGN_CENTER|wx.BOTTOM, border=20)
       self.SetSizer(self.sizerl)


class App(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的 __init__, 否则OnInit方法不会被调用
        #wx.App.__init__(self)         #this sentence has the same features with the next sentence.
        super(self.__class__, self).__init__()
        
    
    def OnInit(self):
        self.version = u"the wxpython course"
        self.title =u"wxpython basic course --" + self.version
        frame = MainFrame(None, -1, self.title)
        frame.Show(True)
        
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
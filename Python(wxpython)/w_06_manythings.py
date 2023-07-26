#!/user/bin/env python           #this sentence is used by Linux
#  静态文本， 控制文本， 对话框， wx.GetApp()函数
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
        self.InitUI()
        # create menu bar
        self.setupMenuBar()

    def InitUI(self):
        """display button features"""
        #Attributes
        self.panel = wx.Panel(self, -1)
        wx.StaticText(self.panel, label="Username", pos = (20,20))  # StaticText 是静态文本框，只能显示，不能交互
        wx.StaticText(self.panel, label="Password", pos = (20,50))
        self._username = wx.TextCtrl(self.panel, pos = (85,15))    # TextCtrl 是控制对话框，可以实现交互
        self._passwd = wx.TextCtrl(self.panel, pos = (85,45), style = wx.TE_PASSWORD)  # wx.TE_PASSWORD can make your input become invisible
        self.submit_btn = wx.Button(self.panel, label = u"submit", pos = (20,80), size = (50,30))
        self.panel.Bind(wx.EVT_BUTTON, self.OnClick, self.submit_btn)
        
    def GetUsername(self):
        return self._username.GetValue()
    
    def GetPassword(self):
        return self._passwd.GetValue()

    def setupMenuBar(self):
        """create menu baru"""
        #create main men
        menubar = wx.MenuBar()
         # children menu (Quit)
        fmenu = wx.Menu()
        fmenu.Append(ID_EXIT, u'QUIT(&Q)', 'Terminate the program')
         # add children menu'Quit' into item(File) of main menu
        menubar.Append(fmenu, u'File(&F)')
        # children menu: About
        hmenu = wx.Menu()
         # add children menu'ABOUT' into item(HELP) of main menu
        hmenu.Append(ID_ABOUT, u'ABOUT(&A)', 'More information about this program')
        menubar.Append(hmenu, u'HELP(&H)')

        self.SetMenuBar(menubar)   #!! add the whole menu block into our Frame.
        # bind the action for the children menu of the main menu
        wx.EVT_MENU(self, ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        wx.EVT_CLOSE(self, self.OnCloseWindow)

    def OnClick(self, event):
        if event.GetEventObject() == self.submit_btn:
            dlg = LoginDialog(None, -1)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            print("No button is clicked.")

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

class LoginDialog(wx.Dialog):
    def __init__(self, parent, id):
        super(LoginDialog, self).__init__(parent, id, u'display',size=(200,200))   #  wx.LoginDialog.__init__(self) / super(self.__class__, self).__init__(parent, id, u'display',size=(200,200))
        self.app = wx.GetApp()  # 类似一个指针，会让之后的self.app指向下面的 class App里的内容
        #Attributes
        self.panel = self.app.frame
        #layout
        self._username_dlg = wx.StaticText(self, label = u"User Name: " + self.GetUsername(), pos = (20,20))
        self._apassword_dlg = wx.StaticText(self, label = u"Password: " + self.GetPassword(), pos = (20,50))
        wx.Button(self, wx.ID_OK, pos = (20,80))

    def GetUsername(self):
        return self.panel.GetUsername()

    def GetPassword(self):
        return self.panel.GetPassword()



class App(wx.App):
    def __init__(self):
        # 如果要重写 __init__, 必须调用wx.App的 __init__, 否则OnInit方法不会被调用
        #wx.App.__init__(self)         #this sentence has the same features with the next sentence.
        super(self.__class__, self).__init__()
        
    
    def OnInit(self):
        self.version = u"the wxpython course"
        self.title =u"wxpython basic course --" + self.version
        self.frame = MainFrame(None, -1, self.title)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
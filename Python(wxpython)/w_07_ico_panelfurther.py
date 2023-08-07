#!/user/bin/env python           #this sentence is used by Linux
#  ico图表实现，wx.panel的进一步学习
import wx
import time
import os

from wx.core import ID_ABOUT, ID_EXIT, version

Version = "0.1"
ReleaseDate = "14/07/2021"

cwd = os.getcwd()   # get the path of the current py/exe file.

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
        # add icon for app
        self.setupIcon()

    def InitUI(self):
        """display button features"""
        #Attributes
        self.panel = MyPanel(self, -1)
        wx.StaticText(self.panel, label="Username", pos = (20,20))  # StaticText 是静态文本框，只能显示，不能交互
        wx.StaticText(self.panel, label="Password", pos = (20,50))
        self.panel._username = wx.TextCtrl(self.panel, pos = (85,15))    # TextCtrl 是控制对话框，可以实现交互
        self.panel._passwd = wx.TextCtrl(self.panel, pos = (85,45), style = wx.TE_PASSWORD)  # wx.TE_PASSWORD can make your input become invisible
        self.panel.submit_btn = wx.Button(self.panel, label = u"submit", pos = (20,80), size = (50,30))
        self.Bind(wx.EVT_BUTTON, self.panel.OnClick, self.panel.submit_btn)
        
    def GetUsername(self):
        return self.panel._username.GetValue()
    
    def GetPassword(self):
        return self.panel._passwd.GetValue()

    def setupMenuBar(self):
        """create menu baru"""
        #create main men
        menubar = wx.MenuBar()
         # children menu (Quit)
        fmenu = wx.Menu()  #  此时开始设置的就是 菜单栏中，一级菜单fmenu 的属性，以及它下面 子菜单的 属性， 直到菜单栏中的另一个一级菜单项目（hmenu）开始设置为止
        quit_menu = wx.MenuItem(fmenu, ID_EXIT, u'QUIT(&Q)')  # 此句 和 之前05课程中的添加语句不一样，是其拆解后的前半部分功能，旨在指明 quit_menu 是 fmenu的子菜单项目，并将这个子菜单 赋值给 quit_menu，便于后面操作
        quit_menu.SetBitmap(wx.Bitmap('./source/point.png'))   # add a icon for quit menu
        fmenu.AppendItem(quit_menu) #把完成配置后的 子菜单item 正式添加给 一级菜单 fmenu
        #fmenu.Append(ID_EXIT, u'QUIT(&Q)', 'Terminate the program')
         # add children menu'Quit' into item(File) of main menu
        menubar.Append(fmenu, u'File(&F)')    #把完成配置的 一级菜单 fmenu 添加到 菜单栏，并给予名字和快捷键
        # children menu: About
        hmenu = wx.Menu()
        about_menu = wx.MenuItem(hmenu, ID_ABOUT, u'ABOUT(&A)')
        about_menu.SetBitmap(wx.Bitmap('./source/about.jpg'))
        hmenu.AppendItem(about_menu)
         # add children menu'ABOUT' into item(HELP) of main menu
        #hmenu.Append(ID_ABOUT, u'ABOUT(&A)', 'More information about this program')
        menubar.Append(hmenu, u'HELP(&H)')

        self.SetMenuBar(menubar)   #!! add the whole menu block into our Frame. 即完成菜单栏设置的意思
        # bind the action for the children menu of the main menu
        wx.EVT_MENU(self, ID_EXIT, self.OnMenuExit)
        wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        wx.EVT_CLOSE(self, self.OnCloseWindow)

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

    def setupIcon(self):
        """add icon for app"""
        self.img_path = os.path.abspath("./source/tubiao.png") 
        icon = wx.Icon(self.img_path, type = wx.BITMAP_TYPE_PNG)  # 将png格式的图片转化为icon位置识别的格式
        self.SetIcon(icon)  #将转换好的图片 放到icon 位置显示，即 完成设置程序左上角图标


class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        super(MyPanel, self).__init__(parent, id)

    # 到这个07课程位置，这里 GetUserName，GetPassword 都是没有用的，因为没有地方调用他们，
    # 同时，这里面的self._username和self._passwd也是错误且没有用的，因为此时的self指向class MyPanel, 但是此时的该class里面并没有这两个参数。
    def GetUserName(self):             
        return self._username.GetValue()

    def GetPassword(self):
        return self._passwd.GetValue()

    def OnClick(self, event):
        if event.GetEventObject() == self.submit_btn:
            dlg = LoginDialog(None, -1)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            print("No button is clicked.")

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
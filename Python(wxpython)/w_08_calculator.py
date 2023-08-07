#!/user/bin/env python           #this sentence is used by Linux
#  calculator
import wx
import time
import os

from panel.TestPanel1 import MyPanel

from wx.core import Font, ID_ABOUT, ID_CANCEL, ID_EXIT, version

Version = "0.1"
ReleaseDate = "14/07/2021"

cwd = os.getcwd()   # get the path of the current py/exe file.

ID_EXIT = 200
ID_ABOUT = 201
ID_CALC = 300

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (310,450))
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
        
        #define global variable 
        global ID_CALC

        #define the variable which should be stored in text.
        self.panel.resultStr = ''

        #define contral variable
        self.panel.calcResult = wx.TextCtrl(self.panel, -1, '', pos=(20,10), size=(250,50), style=wx.TE_MULTILINE|wx.TE_RICH2)  #????!! style=wx.TE_MULTILINE|wx.TE_RICH2 represent we can edit mutiple lines
        font = wx.Font('18') 
        self.panel.calcResult.SetFont(font)

        # place the operation button 
        button_list = ['7','8','9','DEL','AC','4','5','6','*','/','1','2','3','+',\
                       '-','0','%','PI','e','sqrt','^','sin','cos','tan','log','ln',\
                        '(',')','.','=']

           # 下面的 enumerate(list) 是一个内置的 将列表转化为枚举的 函数，这个枚举可以自动给列表加上从 0 开始的 序号，分别对应list 里面的 第1，,2...位，所以在for循环这个枚举对象的时候要 单独 随 列表内元素 一起遍历 对应的序号（这里是 i）
        for i, button in enumerate(button_list):
            wx.Button(self.panel, ID_CALC, label="{}".format(button), pos = (20+50*(i%5), 70+50*(i//5)), size=(50,40))  # !!!空间整齐排列方式：  pos = (x, y) 是表示位置坐标，此行中的运用数学方法，将初始位置设为（20,70） 然后利用取余 和 除法取整 （python的取整方式以及/ 和// 的应用可见收藏贴）
            self.Bind(wx.EVT_BUTTON, self.panel.OnCalcClick, id=ID_CALC)   # 首先是利用 wx.EVT_BUTTON 确定这是一个关于按钮 和 按钮点击事件的绑定动作，其次是，当点击事件发生在id为 ID_CALC 的按钮时， 函数OnCalcClick将会被触发。
            ID_CALC = ID_CALC + 1
       
    def setupMenuBar(self):
        """create menu baru"""
        #create main men
        menubar = wx.MenuBar()
         # children menu (Quit)
        fmenu = wx.Menu()  #  此时开始设置的就是 菜单栏中，一级菜单fmenu 的属性，以及它下面 子菜单的 属性， 直到菜单栏中的另一个一级菜单项目（hmenu）开始设置为止
        quit_menu = wx.MenuItem(fmenu, ID_EXIT, u'QUIT(&Q)')  # 此句 和 之前05课程中的添加语句不一样，是其拆解后的前半部分功能，旨在指明 quit_menu 是 fmenu的子菜单项目，并将这个子菜单 赋值给 quit_menu，便于后面操作
        quit_menu.SetBitmap(wx.Bitmap('./source/quit.jpg'))   # add a icon for quit menu
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
        # self.img_path = os.path.abspath(cwd + "\\source\\tubiao.png")
        icon = wx.Icon(self.img_path, type = wx.BITMAP_TYPE_PNG)  # 将png格式的图片转化为icon位置识别的格式
        self.SetIcon(icon)  #将转换好的图片 放到icon 位置显示，即 完成设置程序左上角图标




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
        self.frame = MainFrame(None, -1, self.title)
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
from typing import Counter
import wx
import time
import os
from panel.Panelset import PanelSet
from datetime import datetime
from threading import Timer
from wx.core import ID_ABOUT, ID_COPY, ID_EXIT, ID_FIND, ID_INFO, ID_MDI_WINDOW_LAST, ID_NEW, ID_OPEN, ID_PASTE, ID_SAVE, ID_SAVEAS, ID_STOP

############
Version = "0.1"
############


ID_NEW = 200
ID_OPEN = 201
ID_SAVE = 202
ID_SAVEAS = 203
ID_EXIT = 204
ID_INFO = 205
ID_ABOUT = 206
ID_UPLOAD = 207
ID_STOP = 208


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (800,800))
        
        self.InitUI()          # main interface show
        self.createMenuBar()   # start menu bar
        self.createToolBar()   # start tool bar
        self.setupStatusBar()  # start status bar
        self.setupIcon()       # start ico of title
       
### import panelset
    def InitUI(self):
        self.panelset = PanelSet(self,-1)
        
### Menu Bar Part
    # declare the item of menu (including firstlevel and secondlevel)
    def menuData(self):
        return (
                    ( u'File(&F)', 
                     (u'New(&N)',         ID_NEW,     './source/point.png', self.OnMenu),
                     (u'Open(&O)...',     ID_OPEN,    './source/point.png', self.OnMenu),
                     (u'Save(&S)',        ID_SAVE,    './source/point.png', self.OnMenu),
                     (u'Save As(&A)...',  ID_SAVEAS,  './source/point.png', self.OnMenu),
                     (u'',                u'',        u'',                  u'',       ),
                     (u'Quit(&Q)',        ID_EXIT,    './source/point.png', self.OnMenu),
                    ),
                    ( u'Tool(&T)',
                     (u'Copy(&C)',        ID_COPY,     './source/point.png', self.OnMenu),
                     (u'Paste(&P)',       ID_PASTE,    './source/point.png', self.OnMenu),
                     (u'Find(&F)',        ID_FIND,     './source/point.png', self.OnMenu),
                    ), 
                    ( u'Help(&H)',
                     (u'Instruction(&I)', ID_INFO,    './source/point.png', self.OnMenu),
                     (u'About(&A)',       ID_ABOUT,   './source/point.png', self.OnMenu)
                    ), 
               )

    # The function of each menu item
    def OnMenu(self, event):
        ID_MENU_ITEM = (ID_NEW, ID_OPEN, ID_SAVE, ID_SAVEAS, ID_EXIT, ID_INFO, ID_ABOUT, ID_UPLOAD, ID_STOP)
        evt_id = event.GetId()
        if evt_id in ID_MENU_ITEM:
            if evt_id == ID_NEW:
                event.Skip()
            elif evt_id == ID_OPEN:
                event.Skip()
            elif evt_id == ID_SAVE:
                event.Skip()
            elif evt_id == ID_SAVEAS:
                event.Skip()
            elif evt_id == ID_EXIT:
                event.Skip()
            elif evt_id == ID_INFO:
                event.Skip()
            elif evt_id == ID_ABOUT:
                event.Skip()
            elif evt_id == ID_UPLOAD:
                self.uploaddata(5)
            # elif evt_id == ID_STOP:
            #     self.uploaddata(0)
                

            # elif evt_id == ID_STOP:
            #     self.eventstop()
               
    # set up the relationship between menu Bar and menu(firstlevel, secondlevel) ( bracket start)
    def createMenuBar(self):
        """create menu bar and make it display"""
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menu_firstlevel = eachMenuData[0]
            menu_secondlevel = eachMenuData[1:]
            menuBar.Append(self.createMenu(menu_secondlevel), menu_firstlevel)
        self.SetMenuBar(menuBar)

    # complete the menu setting (bracket close)
    def createMenu(self,menuData):
        menu = wx.Menu()
        for eachLabel, eachId, eachico, eachHandler in menuData:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menuItem = wx.MenuItem(menu, eachId, eachLabel)
            menuItem.SetBitmap(wx.Bitmap(eachico))
            menu.AppendItem(menuItem)
            self.Bind(wx.EVT_MENU, eachHandler, menuItem)
        return menu

### Tool Bar Part
    # set up the relationship between Tool Bar and too(firstlevel, secondlevel) ( bracket start)
    # declare the item of tool (including firstlevel and secondlevel)
    def toolData(self):
        return (
                (u'New(&N)',         ID_NEW,      './source/point.png', self.OnMenu),
                (u'Open(&O)...',     ID_OPEN,     './source/point.png', self.OnMenu),
                (u'Save(&S)',        ID_SAVE,     './source/point.png', self.OnMenu),
                (u'Copy(&C)',        ID_COPY,     './source/point.png', self.OnMenu),
                (u'Paste(&P)',       ID_PASTE,    './source/point.png', self.OnMenu),
                (u'Find(&F)',        ID_FIND,     './source/point.png', self.OnMenu),
                (u'Upload(&U)',      ID_UPLOAD,   './source/upload.ico', self.OnMenu),
                (u'Stop(&T)',      ID_STOP,   './source/upload.ico', self.OnMenu)
               )

    def createToolBar(self):
        """create tool bar and make it display"""
        toolBar = wx.ToolBar(self, style=wx.TB_TEXT|wx.HORIZONTAL)
        self.ToolBar = toolBar 
        # toolBar.SetBackgroundColour('Grey')
        for eachLabel, eachId, eachico, eachHandler in self.toolData():
            toolItem =  toolBar.AddTool(eachId, eachLabel, wx.Bitmap(eachico))
            self.Bind(wx.EVT_TOOL, eachHandler, toolItem)
        toolBar.Realize()

### Status Bar Part
    # create statusBar and make it display
    def setupStatusBar(self):
        """create state bar"""
        self.sbar = self.CreateStatusBar(3)   # create status of window and separate it into 3 parts
        self.SetStatusWidths([-2,-2,-1])      # the status is divdided into two parts, the ratio of two is 2:2:1
        self.SetStatusText("Ready",0)      # 0 represent the first position of the status
        self.SetStatusText(u"",1)          # 1 represent the second position of the status

        #timer: set the time part in statusbar and make time change one second by one second.
        self.timer = wx.PyTimer(self.Notify)  # derived from wx.Timer
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)     # 1000 means we begin with 1 second, and TIMER_CONTINUOUS can keep it always run....
        self.Notify()
    
    def Notify(self):
        """set the format of the date in statusbar, place the time part in the third part of statusbar"""
        t = time.localtime(time.time())   # t 将会以时间戳的形式被赋值
        st = time.strftime('%d/%m/%Y %H:%M:%S', t)  # 将 t 的时间戳转化为正常时间格式
        self.SetStatusText(st, 2)   #将这个时间 显示在 status 的第二个位置上。

### app title ico setting
    def setupIcon(self):
        """add icon for app"""
        self.img_path = os.path.abspath("./source/point.png") 
        icon = wx.Icon(self.img_path, type = wx.BITMAP_TYPE_PNG)  
        self.SetIcon(icon)  

### function for menu and tool
    def uploaddata(self, inc): 
        self.panelset.textPanel.TXResult.AppendText(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        time_event = Timer(inc, self.uploaddata, (inc,))
        time_event.start()


    


class App(wx.App):
    def __init__(self):
        #wx.App.__init__(self)         #this sentence has the same features with the next sentence.
        super(self.__class__, self).__init__()
        
    
    def OnInit(self):
        self.version = u"version 0.1"
        self.title =u"Automatic Data Upload --" + self.version
        frame = MainFrame(None, -1, self.title)
        frame.Show(True)
        
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()


    
        

    
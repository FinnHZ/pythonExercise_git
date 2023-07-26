


import wx
import time
import os, sys
from panel.notebook import FXNoteBook

from wx.core import ID_ABOUT, ID_COPY, ID_CUT, ID_DELETE, ID_EXIT, ID_FIND, ID_NEW, ID_OPEN, ID_PASTE, ID_REPLACE, ID_SAVE, ID_SAVEAS, ID_SELECTALL, ID_UNDO, MessageDialog

#  menu, menubar, wx.MessageDialog, wx.FileDialog(和open, save等功能有关)


Version = "0.1"
ReleaseDate = "14/07/2021"

cwd = os.getcwd()   # get the path of the current py/exe file.

ID_EXIT = 200
ID_ABOUT = 201
ID_NEW = 202
ID_OPEN = 203
ID_OPEN_DIR = 204
ID_SAVE = 205
ID_SAVE_AS = 206
ID_UNDO = 207
ID_CUT = 208
ID_COPY = 209
ID_PASTE = 210
ID_DELETE = 211
ID_FIND = 212
ID_FIND_NEXT = 213
ID_REPLACE = 214
ID_SELECT_ALL = 215


class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (310,480))
         # create state bar
        self.setupStatusBar()
        # display button features
        self.InitUI()
        # create menu bar
        self.setupMenuBar()
        # add icon for app
        self.setupIcon()

    def InitUI(self):
        self.fxnotebook = FXNoteBook(self,-1)
    
    def setupMenuBar(self):
        """create menu baru"""
        #  summary: wxpython里面设置从属关系，子项目先设置绑定到 父项目，所有子项目相关设置完了之后，最后，父项目 还要通过Set/Add/Append等语句确认领养 子项目，才能构成完整的从属关系，并执行成功。

        ###create main men
        menubar = wx.MenuBar()

        ## create file item
        file_menu = wx.Menu()  #  此时开始设置的就是 菜单栏中，一级菜单fmenu 的属性，以及它下面 子菜单的 属性， 直到菜单栏中的另一个一级菜单项目（hmenu）开始设置为止
       
        # create : create new page(file) feature
        new_menu = wx.MenuItem(file_menu, ID_NEW, u'New(&N)') #
        new_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        file_menu.AppendItem(new_menu)
        self.Bind(wx.EVT_MENU, self.OnNewFile, new_menu)

        # create :  open file feature
        open_menu = wx.MenuItem(file_menu, ID_OPEN, u'Open(&O)') #
        open_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        file_menu.AppendItem(open_menu)
        self.Bind(wx.EVT_MENU, self.OnOpen, open_menu)  # 另一种形式（以此类推）： wx.EVT_MENU(self, ID_OPEN, self.OnOpen)

        # create :  save file feature
        save_menu = wx.MenuItem(file_menu, ID_SAVE, u'Save(&S)') #
        save_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        file_menu.AppendItem(save_menu)
        self.Bind(wx.EVT_MENU, self.OnSave, save_menu)

        # insert a separator(line)
        file_menu.AppendSeparator()   

        # create :  Quit feature 
        quit_menu = wx.MenuItem(file_menu, ID_EXIT, u'QUIT(&Q)')  # 此句 和 之前05课程中的添加语句不一样，是其拆解后的前半部分功能，旨在指明 quit_menu 是 fmenu的子菜单项目，并将这个子菜单 赋值给 quit_menu，便于后面操作
        quit_menu.SetBitmap(wx.Bitmap('./source/point.png'))   # add a icon for quit menu
        file_menu.AppendItem(quit_menu)
        self.Bind(wx.EVT_MENU, self.OnQuit, quit_menu)

        ## this block end: add 'file' item into menu bar
        menubar.Append(file_menu, u'File(&F)')

        ## create edit item
        edit_menu = wx.Menu()

        # create: undo feature
        undo_menu = wx.MenuItem(edit_menu, ID_UNDO, u'Undo(&U)') #
        undo_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(undo_menu)

        # insert a separator(line)
        edit_menu.AppendSeparator() 

        # create: cut feature
        cut_menu = wx.MenuItem(edit_menu, ID_CUT, u'Cut(&T)') #
        cut_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(cut_menu)
        
        # create: copy feature
        copy_menu = wx.MenuItem(edit_menu, ID_COPY, u'Copy(&C)') #
        copy_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(copy_menu)

        # create: paste feature
        paste_menu = wx.MenuItem(edit_menu, ID_PASTE, u'Paste(&P)') #
        paste_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(paste_menu)

        # create: delete feature
        del_menu = wx.MenuItem(edit_menu, ID_DELETE, u'Delete(&L)') #
        del_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(del_menu)

        # create: find feature
        find_menu = wx.MenuItem(edit_menu, ID_FIND, u'Find(&F)') #
        find_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(find_menu)

        # create: find next feature
        find_next_menu = wx.MenuItem(edit_menu, ID_FIND_NEXT, u'Find Next(&N)') #
        find_next_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(find_next_menu)

        # create: replace feature
        replace_menu = wx.MenuItem(edit_menu, ID_REPLACE, u'Replace(&R)') #
        replace_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(replace_menu)

        # insert a separator(line)
        edit_menu.AppendSeparator() 

        # create: select all feature
        select_all_menu = wx.MenuItem(edit_menu, ID_SELECT_ALL, u'Select All(&A)') #
        select_all_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        edit_menu.AppendItem(select_all_menu)
        self.Bind(wx.EVT_MENU, self.OnSelectAll, select_all_menu)
   
        ## this block end: add 'edit' item into menu bar
        menubar.Append(edit_menu, u'Edit(&E)')

        ## create help item
        help_menu = wx.Menu()

        # create: about feature
        about_menu = wx.MenuItem(help_menu, ID_ABOUT, u'About(&A)')
        about_menu.SetBitmap(wx.Bitmap('./source/point.png'))
        help_menu.AppendItem(about_menu)
        self.Bind(wx.EVT_MENU, self.OnMenuAbout, about_menu)   #wx.EVT_MENU(self, ID_ABOUT, self.OnMenuAbout)
        
        ## this block end: add 'edit' item into menu bar
        menubar.Append(help_menu, u'Help(&H)')  

        ### menubar set completed
        self.SetMenuBar(menubar)   #这一步表示，菜单栏 整个 从属关系 设置完毕，后面的代码，可以更改事件绑定，但是不会影响菜单从属关系绑定

        wx.EVT_CLOSE(self, self.OnCloseWindow)

    def setupStatusBar(self):
        """create state bar"""
        self.sbar = self.CreateStatusBar(3)   # create status of window and separate it into 3 parts
        self.SetStatusWidths([-2,-2,-1])      # the status is divdided into two parts, the ratio of two is 2:2:1
        self.SetStatusText("Ready",0)      # 0 represent the first position of the status
        self.SetStatusText(u"",1)          # 1 represent the first position of the status

        #timer: set the time part in statusbar and make time change one second by one second.
        self.timer = wx.PyTimer(self.Notify)  # derived from wx.Timer
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)     # 1000 means we begin with 1 second, and TIMER_CONTINUOUS can keep it always run....
        self.Notify()
    
    def Notify(self):
        """set the format of the date in statusbar, place the time part in the third part of statusbar"""
        t = time.localtime(time.time())   # t 将会以时间戳的形式被赋值
        st = time.strftime('%d/%m/%Y %H:%M:%S', t)  # 将 t 的时间戳转化为正常时间格式
        self.SetStatusText(st, 2)   #将这个时间 显示在 status 的第二个位置上。

    def OnQuit(self, event):
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

    # create new function !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def OnNewFile(self, event):
        if self.fxnotebook.textPanel.TXResult.IsEmpty() != True:
            dlg = wx.MessageDialog(self, u'Are you sure you want save as no title?', u'notbook', wx.YES_NO | wx.ICON_QUESTION | wx.CANCEL)
            retCode = dlg.ShowModal()
            if retCode == wx.ID_YES:
                self.OnSave(event)  # save
                self.fxnotebook.textPanel.TXResult.SetValue("") # after save, create new file (in fact, it just clear the text.)
            elif retCode == wx.ID_NO:
                self.fxnotebook.textPanel.TXResult.SetValue("")  # clear the text.
            else:
                dlg.Close()  # cancel create new
            dlg.Destroy()    # close the dialog
    
    # save function   !!!!!!!!!!!!!!!!!!!!!!!!
    def OnSave(self, event):
        # determine if there is any content in the text editor 
        if self.fxnotebook.textPanel.TXResult.IsEmpty():
            return
        self.dirname = ""
        filesFilter = "Text(*.txt)|*.txt|Python(*.py)|*.py|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", wildcard=filesFilter, style=wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.fxnotebook.textPanel.TXResult.GetValue())
            f.close()
        dlg.Destroy()
        # reset the title of the notebook
        self.Title = self.filename + u" - NoteBook"
    
    # save as function   !!!!!!!!!!!!!!!!!!!!!!!!
    def OnSaveAs(self, event):
        """save the content of the file / Bind the save part"""
        self.dirname = ""
        filesFilter = "Text(*.txt)|*.txt|Python(*.py)|*.py|All files(*.*)|*.*"
        fd = wx.FileDialog(self, u"Save as...", self.dirname, "", wildcard=filesFilter, style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if fd.ShowModal() == wx.ID_OK:
            self.filename = fd.GetFilename()
            self.dirname = fd.GetDirectory()
            try:
                with open(os.path.join(self.dirname, self.filename), 'w') as f:
                    f.write(self.fxnotebook.textPanel.TXResult.GetValue())
                    f.close()
                    save_msg = wx.MessageDialog(self, u"File has been saved", u"Note")
            except FileNotFoundError:
                save_msg = wx.MessageDialog(self, u"Fail to saved, inavailable path!", u"Note")
        else:
            save_msg =  wx.MessageDialog(self, u"You did not choose the path for saving!", u"Error")
        
        save_msg.ShowModal()
        save_msg.Destroy()

    # open the dialog for choosing file
    def OnOpen(self, e):
        """open a file"""
        self.dirname = ''
        """
           wx.FD_OPEN
           wx.FD_SAVE
           wx.FD_OVERWRITE_PROMPT
           wx.FD_MULTIPLE
           wx.FD_CHANGE_DIR
        """

        filesFilter = "Text(*.txt)|*.txt|Python(*.py)|*.py|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, u"Choose a file", self.dirname, "", wildcard=filesFilter, style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.fxnotebook.textPanel.TXResult.SetValue(f.read())
            f.close()
        dlg.Destroy()
        self.fxnotebook.textPanel.TXResult.SetFocus()
        wx.StaticText(self, label=u"File Name: " + self.filename + u", total " + str(self.fxnotebook.textPanel.TXResult.GetNumberOfLines()) + u" rows", pos=(0,1))


    def OnSelectAll(self, event):
        self.fxnotebook.textPanel.TXResult.SelectAll()




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
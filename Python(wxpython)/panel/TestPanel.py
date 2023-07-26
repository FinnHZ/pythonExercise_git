import wx
import math

ID_CALC = 300

class MyPanel(wx.Panel):   # wx.Panel对应的框架里没有属性 panel
    def __init__(self, parent, id):
        super(MyPanel, self).__init__(parent, id)

        global ID_CALC

        #define the variable which should be stored in text.
        self.resultStr = ''

        #define contral variable
        self.calcResult = wx.TextCtrl(self, -1, '', pos=(20,10), size=(250,50), style=wx.TE_MULTILINE|wx.TE_RICH2)  #????!! style=wx.TE_MULTILINE|wx.TE_RICH2 represent we can edit mutiple lines
        font = wx.Font('18') 
        self.calcResult.SetFont(font)

        vbox = wx.BoxSizer(wx.VERTICAL)  #  表示盒子里 的排列 自上而下  ？？？？？
        vbox.Add(self.calcResult, 0, 20)   #这里先将 可控文本框 添加到 大盒子里vbox？？？？？？？, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL  ???

        # place the operation button 
        button_list = ['7','8','9','DEL','AC','4','5','6','*','/','1','2','3','+',\
                       '-','0','%','PI','e','sqrt','^','sin','cos','tan','log','ln',\
                        '(',')','.','=']
        buttons = []
           # 下面的 enumerate(list) 是一个内置的 将列表转化为枚举的 函数，这个枚举可以自动给列表加上从 0 开始的 序号，分别对应list 里面的 第1，,2...位，所以在for循环这个枚举对象的时候要 单独 随 列表内元素 一起遍历 对应的序号（这里是 i）
        for i, button in enumerate(button_list):
            buttons.append((wx.Button(self,ID_CALC, label="{}".format(button), size=(50,40)), 0, wx.EXPAND))
            self.Bind(wx.EVT_BUTTON, self.OnCalcClick, id=ID_CALC)   # 首先是利用 wx.EVT_BUTTON 确定这是一个关于按钮 和 按钮点击事件的绑定动作，其次是，当点击事件发生在id为 ID_CALC 的按钮时， 函数OnCalcClick将会被触发。
            ID_CALC = ID_CALC + 1
        
        gs = wx.GridSizer(6,5,5,5)  #这里gs是一个新的容器，而GridSizer则是负责规划这个容器里的元素分布位置。前两个参数分别代表 6行， 5列  后两个参数待查询？？？？ 
        gs.AddMany(buttons)   #？？？？？？# AddMany可以将一个列表添加到一个容器中。

        vbox.Add(gs, 0,  20) # 这里把按键框部分添加到 大盒子里 vbox wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL ???
        self.SetSizer(vbox)

    def setText(self, value):
        """set the value of TextCtrl"""
        self.calcResult.SetValue(value)

    def OnCalcClick(self,event):
        print(event.GetId())
        mathFunc = ['sqrt', 'sin', 'cos', 'tan']
        result = 'Error'
        if event.GetEventObject().GetLabel() == '=':
            print("=")
            for func in mathFunc:
                if func in self.resultStr:
                    try:
                        result = str(eval('math.'+self.resultStr))  # eval()可以将括号内的字符串和表达式组合成一个表达式形式的对象，并执行
                        break
                    except: pass
            if '^' in self.resultStr:
                try:
                    temp = self.resultStr.split('^')  # xxxx.split('^') means, separate the content of 'xxxxx' according to the symbol '^', and return a list, the list will contain the separated-element one by one.
                    result = str(eval('pow(' + temp[0] + ',' + temp[1] + ')'))
                except: pass
            elif 'ln' in self.resultStr:
                try:
                    result = str(eval('math.log' + self.resultStr[2:]))
                except: pass
            elif 'log' in self.resultStr:
                try:
                    result = str(eval('math.log' + self.resultStr[3:] + '/math.log(10)'))
                except: pass
            else:
                try:
                    result = str(eval(self.resultStr))
                except: pass
            
            self.resultStr = result
            self.setText(result)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'AC':
            """click the button 'AC' to clear the screen"""
            self.calcResult.SetValue('')
            self.resultStr = ''
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'DEL':
            """click the button 'DEL' to Undo"""
            self.resultStr = self.resultStr[:-1]
            self.setText(self.resultStr)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'e':
            """ e = math.e """
            self.resultStr += str(math.e)
            self.setText(self.resultStr)
            event.Skip()
        elif event.GetEventObject().GetLabel() == 'PI':
            """pi = 3.1415926....."""
            self.resultStr += str(math.pi)
            self.setText(self.resultStr)
            event.Skip()
        else:
            self.resultStr += event.GetEventObject().GetLabel()
            self.setText(self.resultStr)
            event.Skip()
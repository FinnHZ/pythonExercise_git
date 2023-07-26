import wx
import math

class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        super(MyPanel, self).__init__(parent, id)

        

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
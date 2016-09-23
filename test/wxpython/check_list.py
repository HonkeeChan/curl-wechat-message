import wx  
class CheckListFrame(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'Choice Example',   
                size=(250, 200))  
        self.pannel = wx.Panel(self, -1)  
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',  
                      'six', 'seven', 'eight']  
        wx.StaticText(self.pannel, -1, "Select :", (15, 20))  
        self.checkListBox = wx.CheckListBox(self.pannel, -1, (85, 18), choices=sampleList)  

        menubar=wx.MenuBar()  
        clickBtn=wx.Menu()  
        clickBtn.Append(101,'&Open','Open a new document')  
        menubar.Append(clickBtn,'&File')  
        wx.EVT_TOOL( self, 101, self.OnClick)
        self.SetMenuBar( menubar )

        self.statusbar = self.CreateStatusBar()  
        

    def OnClick(self, event):
        self.statusbar.SetStatusText( 'click' )  
        print self.checkListBox.GetChecked()

        sampleList = ['zero', 'one', 'two']  
        #self.pannel.RemoveChild( self.checkListBox)
        self.checkListBox.Destroy()
        # self.pannel.RemoveChild(self.checkListBox)
        #self.pannel = wx.Panel(self, -1)  
        
        self.checkListBox = wx.CheckListBox(self.pannel, -1, (85, 18), choices=sampleList) 
        # self.checkListBox.Create(self.pannel, -1, (85, 18), choices=sampleList)

        # self.pannel.Refresh()
        # self.pannel.Update()
        self.Layout()

if __name__ == '__main__':  
    app = wx.App()  
    CheckListFrame().Show()  
    app.MainLoop()  
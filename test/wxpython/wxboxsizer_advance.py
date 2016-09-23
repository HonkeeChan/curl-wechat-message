import wx  
class MyFrame( wx.Frame ):  
    def __init__( self, parent, ID, title ):  
        wx.Frame.__init__(self,parent,ID,title,(-1,-1),wx.Size(450,300))  
          
        panel = wx.Panel(self,-1)  
        box = wx.BoxSizer( wx.HORIZONTAL )  
          
        box.Add( wx.Button( panel, -1, 'Button1' ), 1, wx.ALL, 5 )  
        box.Add( wx.Button( panel, -1, 'Button2' ), 1, wx.EXPAND )  
        box.Add( wx.Button( panel, -1, 'Button3' ), 0, wx.ALIGN_CENTER )  
          
        panel.SetSizer( box )  
        self.Center()  
  
class MyApp( wx.App ):  
    def OnInit( self ):  
        frame = MyFrame( None, -1, 'layout3.py' )  
        frame.Show( True )  
        return True  
      
app = MyApp( 0 )  
app.MainLoop()  
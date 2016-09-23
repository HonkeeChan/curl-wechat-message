import wx  
class MyMenu( wx.Frame ):  
    def __init__(self,parent,ID,title):  
        wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(200, 150))  
        menubar=wx.MenuBar()  
        file=wx.Menu()  
        edit=wx.Menu()  
        help=wx.Menu()

        file.Append(101,'&Open','Open a new document')  
        file.Append(102,'&Save','Save the document')  
        file.AppendSeparator()  
        quit=wx.MenuItem(file,105,'&Quit\tCtrl+Q','Quit the Application', wx.ITEM_CHECK)  
        # quit.SetBitmap(wx.Image('stock_exit-16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())  
        file.AppendItem(quit)  
        menubar.Append(file,'&File')  
        menubar.Append(edit,'&Edit')  
        menubar.Append(help,'&Help')  

        submenu = wx.Menu()
        submenu.Append( 301, 'radio item1', kind= wx.ITEM_RADIO )
        submenu.Append( 302, 'radio item2', kind=wx.ITEM_RADIO )
        submenu.Append( 303, 'radio item3', kind=wx.ITEM_RADIO )
        edit.AppendMenu( 203, 'submenu', submenu )
        
        self.SetMenuBar( menubar )  
  
class MyApp(wx.App):  
    def OnInit(self):  
        frame=MyMenu(None,-1,'menu1.py')  
        frame.Show(True)  
        return True  
          
app=MyApp(0)  
app.MainLoop() 
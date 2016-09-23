#!/usr/bin/env python  
# FileName: toolbar.py  
import wx  
class MyToolBar( wx.Frame ):  
      
    def __init__( self, parent, ID, title ):  
        wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 350, 250 ) )  
          
        vbox = wx.BoxSizer( wx.VERTICAL )  
        toolbar = wx.ToolBar( self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER )  
        toolbar.AddSimpleTool( 1, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'New', '' )  
        toolbar.AddSimpleTool( 2, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Opne', '' )  
        toolbar.AddSimpleTool( 3, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Save', '' )  
        toolbar.AddSeparator()  
        toolbar.AddSimpleTool( 4, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Exit', '' )  
        toolbar.Realize()  
          
        vbox.Add( toolbar, 0, border=5 )  
        self.SetSizer( vbox )  
        self.statusbar = self.CreateStatusBar()  
          
        self.Centre()  
          
        wx.EVT_TOOL( self, 1, self.OnNew )  
        wx.EVT_TOOL( self, 2, self.OnOpen )  
        wx.EVT_TOOL( self, 3, self.OnSave )  
        wx.EVT_TOOL( self, 4, self.OnExit )  
      
    def OnNew( self, event ):  
        self.statusbar.SetStatusText( 'New Command' )  
      
    def OnOpen( self, event ):  
        self.statusbar.SetStatusText( 'Open Command' )  
      
    def OnSave( self, event ):  
        self.statusbar.SetStatusText( 'Save Command' )  
      
    def OnExit( self, event ):  
        self.Close()  
      
class MyApp( wx.App ):  
    def OnInit( self ):  
        frame = MyToolBar( None, -1, ' toolbar.py' )  
        frame.Show( True )  
        return True  
      
app = MyApp( 0 )  
app.MainLoop()  
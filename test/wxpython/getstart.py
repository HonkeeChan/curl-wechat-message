import wx  
app = wx.PySimpleApp()  
frame = wx.Frame( None, -1, 'hello' )  
frame.SetToolTip( wx.ToolTip( 'This is a frame' ) )  
frame.SetCursor( wx.StockCursor( wx.CURSOR_MAGNIFIER ) )  
frame.SetPosition( wx.Point( 50, 50 ) )  
frame.SetSize( wx.Size( 300, 250 ) )  
# frame.SetTitle( 'simple2.py' )  
frame.Center()
frame.Show()  
app.MainLoop() 
import wx
import images

class ToolbarFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars', size=(600, 700))
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(), "New", "Long help for 'New'")
        toolbar.Realize()
        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "&Cut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        self.SetMenuBar(menuBar)

        self.text = wx.TextCtrl(self.panel, wx.NewId(), "Type assy here", size=(150,-1), pos=(20,30), style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.Onenter, self.text)
        goButton = wx.Button(self.panel, -1, "GO!", pos=(100,100))
        self.Bind(wx.EVT_BUTTON, self.Ongo, goButton)
        self.static = wx.StaticText(self.panel, wx.NewId(), "", size=(200,-1), pos=(200,200))

        self.listBox = wx.ListBox(self.panel, -1, (150,250), (100,150), [] , style = wx.LB_SINGLE | wx.LB_SORT)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.Ondclick, self.listBox)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.Onkey, self.listBox)


    def Ongo(self, event):
        self.panel.SetBackgroundColour('Green')
        self.panel.Refresh()
        self.static.SetLabel('Hi')
        self.static.SetToolTipString(self.text.GetValue())
        self.listBox.Append(self.text.GetValue())
        #self.listBox.Refresh()
        #self.static.Refresh()

    def Ondclick(self, event):
	    print self.listBox.GetStringSelection()

    def Onenter(self, event):
        self.listBox.Append(self.text.GetValue())
        self.listBox.SetFocus()

    def Onkey(self, event):
        print event.GetItem()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
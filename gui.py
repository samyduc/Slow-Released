# TAD courtesy #

# deckardfr aka Samy Duc #
# mail : samy.duc@gmail.com !

# fork me !

import wx

class Config(wx.Panel):
	def __init__(self, parent, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
		# sizer
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		grid = wx.GridBagSizer(hgap=5, vgap=9)
		hSizer = wx.BoxSizer(wx.HORIZONTAL)
		
		# config menu
		self.helper_label = wx.StaticText(self, label="Field are set with default value")
		grid.Add(self.helper_label, pos=(0,1), span=(1,4))
		
		self.url_label = wx.StaticText(self, label="URL")
		grid.Add(self.url_label, pos=(2,2))
		self.url_edit = wx.TextCtrl(self, value="http://127.0.0.1:80/form.html", size=(240,-1))
		grid.Add(self.url_edit, pos=(2,3))
		
		self.delay_label = wx.StaticText(self, label="Delay")
		grid.Add(self.delay_label, pos=(3,2))
		self.delay_edit = wx.TextCtrl(self, value="300", size=(240,-1))
		grid.Add(self.delay_edit, pos=(3,3))
		self.delay_check = wx.CheckBox(self, label="random")
		grid.Add(self.delay_check, pos=(3,4))
		
		self.useragent_label = wx.StaticText(self, label="User-Agent")
		grid.Add(self.useragent_label, pos=(4,2))
		self.useragent_edit = wx.TextCtrl(self, value="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)", size=(240,-1))
		grid.Add(self.useragent_edit, pos=(4,3))
		self.useragent_check = wx.CheckBox(self, label="random")
		self.useragent_check.SetValue(True)
		grid.Add(self.useragent_check, pos=(4,4))
		
		self.contentlength_label = wx.StaticText(self, label="Content-Length")
		grid.Add(self.contentlength_label, pos=(5,2))
		self.contentlength_edit = wx.TextCtrl(self, value="1000", size=(240,-1))
		grid.Add(self.contentlength_edit, pos=(5,3))
		self.contentlength_check = wx.CheckBox(self, label="random")
		self.contentlength_check.SetValue(True)
		grid.Add(self.contentlength_check, pos=(5,4))
		
		self.payload_label = wx.StaticText(self, label="Payload")
		grid.Add(self.payload_label, pos=(6,2))
		self.payload_edit = wx.TextCtrl(self, value="abcdefg", size=(240,-1))
		grid.Add(self.payload_edit, pos=(6,3))
		self.payload_check = wx.CheckBox(self, label="random")
		self.payload_check.SetValue(True)
		grid.Add(self.payload_check, pos=(6,4))
		
		self.payload_label = wx.StaticText(self, label="Threads")
		grid.Add(self.payload_label, pos=(7,2))
		self.payload_edit = wx.TextCtrl(self, value="5", size=(240,-1))
		grid.Add(self.payload_edit, pos=(7,3))
		
		self.mode_radio = ['probe', 'probe + attack', 'attack']
		self.rb = wx.RadioBox(self, label="Mode", choices=self.mode_radio,  majorDimension=3,style=wx.RA_SPECIFY_COLS)
		grid.Add(self.rb, pos=(8,2), span=(1,4))
		
		self.button =wx.Button(self, label="Ok")
		grid.Add(self.button, pos=(9,4), span=(1,4))
		
		#self.Show()
		hSizer.Add(grid, 0, wx.ALL, 5)
		mainSizer.Add(hSizer, 0, wx.ALL, 5)
		self.SetSizerAndFit(mainSizer)
		
		
class Stats(wx.Panel):
	def __init__(self, parent, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		
class About(wx.Panel):
	def __init__(self, parent, *args, **kwargs):
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.parent = parent

	
		

class MainFrame(wx.Frame):
	""" We simply derive a new class of Frame. """
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(500,430))
		#self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		
		self.CreateStatusBar()
		
		self.tabbed = wx.Notebook(self, -1, style=(wx.NB_TOP))
		self.config_panel = Config(self.tabbed, -1)
		self.stats_panel = wx.Panel(self.tabbed, -1)
		self.tabbed.AddPage(self.config_panel, "Configuration")
		self.tabbed.AddPage(self.stats_panel, "Stats")
		self.tabbed.AddPage(self.stats_panel, "HTTP response")	
		
		file_menu= wx.Menu()
		#filemenu.AppendSeparator()
		exit_item = file_menu.Append(wx.ID_EXIT,"&Exit","I hope you enjoy your ride")
		
		about_menu= wx.Menu()
		self.ID_SAVE_ME = wx.ID_HIGHEST + 1
		technical_item = about_menu.Append(self.ID_SAVE_ME, "&Technical insight", "Some stuff about slow Post")
		about_item = about_menu.Append(wx.ID_ABOUT, "&About", "About me and my crew")
		
		menuBar = wx.MenuBar()
		menuBar.Append(file_menu,"&File")
		menuBar.Append(about_menu,"&Help")
		
		self.SetMenuBar(menuBar)
		
		self.Bind(wx.EVT_MENU, self.onExit, exit_item)
		self.Bind(wx.EVT_MENU, self.onTechnical, technical_item)
		self.Bind(wx.EVT_MENU, self.onAbout, about_item)
		
		self.Fit()
		self.Show(True)
	
	def onExit(self, event):
		self.Close(True)
	
	def onAbout(self, event):
		dlg = wx.MessageDialog(self, message='A completely useless message', caption='A Message Box', style=wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	
	def onTechnical(self, event):
		print("lol")
		

app = wx.App(False)
frame = MainFrame(None, 'Slow Released Tool Kit from deckardfr courtesy of TAD')
app.MainLoop()
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Home page", pos = wx.DefaultPosition, size = wx.Size( 498,225 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"LOGIN ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Sebagai Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Sebagai Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		gSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"ADMIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetBackgroundColour( wx.Colour( 0, 255, 64 ) )

		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"SISWA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )

		gSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.btn_admin )
		self.m_button2.Bind( wx.EVT_BUTTON, self.btn_siswa )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_admin( self, event ):
		event.Skip()

	def btn_siswa( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login", pos = wx.DefaultPosition, size = wx.Size( 360,229 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"SILAHKAN LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		fgSizer1.Add( self.m_button3, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.btn_login )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Registrasi", pos = wx.DefaultPosition, size = wx.Size( 556,672 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Data Diri Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer5.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nama Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl111 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl111, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"No. Telpon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Agama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer2.Add( self.m_staticText13, 0, wx.ALL, 5 )

		m_choice2Choices = [ u"ISLAM", u"BUDHA", u"KONGHUCU", u"HINDU", u"KRISTEN", u"KATOLIK" ]
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 3 )
		gSizer2.Add( self.m_choice2, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )

		m_choice3Choices = [ u"PRIA", u"WANITA" ]
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 1 )
		gSizer2.Add( self.m_choice3, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Nama Ayah Kandung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer2.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		gSizer2.Add( self.m_staticText23, 0, wx.ALL, 5 )

		m_choice4Choices = [ u"PNS", u"SWASTA", u"LAINNYA" ]
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 2 )
		gSizer2.Add( self.m_choice4, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Penghasilan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		gSizer2.Add( self.m_staticText24, 0, wx.ALL, 5 )

		m_choice5Choices = [ u"<1.000.000", u"1.500.000 - 3.000.000", u"> 3.000.000" ]
		self.m_choice5 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 2 )
		gSizer2.Add( self.m_choice5, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Nama Ibu Kandung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gSizer2.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		gSizer2.Add( self.m_staticText25, 0, wx.ALL, 5 )

		m_choice6Choices = [ u"PNS", u"SWASTA", u"LAINNYA", wx.EmptyString ]
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 1 )
		gSizer2.Add( self.m_choice6, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"penghasilan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		gSizer2.Add( self.m_staticText26, 0, wx.ALL, 5 )

		m_choice7Choices = [ u"< 1.000.000", u"1.500.000 - 3.000.000", u"> 3.000.000" ]
		self.m_choice7 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice7Choices, 0 )
		self.m_choice7.SetSelection( 2 )
		gSizer2.Add( self.m_choice7, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"No. Telpon Orang Tua", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gSizer2.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Alamat Orangtua", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		gSizer2.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer2.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button5, 0, wx.ALL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer5.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.SubmitFrame3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def SubmitFrame3( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog6
###########################################################################

class MyDialog6 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Notifikasi", pos = wx.DefaultPosition, size = wx.Size( 330,144 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"SELAMAT ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer7.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"ANDA BERHASIL REGISTRASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		bSizer7.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button6, 0, wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.btn_logoutD6 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_logoutD6( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"DATA SISWA YANG REGISTRASI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		bSizer8.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 10, 15 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( True )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"Nama Siswa" )
		self.m_grid1.SetColLabelValue( 1, u"Tanggal Lahir" )
		self.m_grid1.SetColLabelValue( 2, u"NIK" )
		self.m_grid1.SetColLabelValue( 3, u"No. Telpon" )
		self.m_grid1.SetColLabelValue( 4, u"Agama" )
		self.m_grid1.SetColLabelValue( 5, u"Jenis Kelamin" )
		self.m_grid1.SetColLabelValue( 6, u"Alamat" )
		self.m_grid1.SetColLabelValue( 7, u"Nama Ayah" )
		self.m_grid1.SetColLabelValue( 8, u"Pekerjaan Ayah" )
		self.m_grid1.SetColLabelValue( 9, u"Penghasilan Ayah" )
		self.m_grid1.SetColLabelValue( 10, u"Nama Ibu" )
		self.m_grid1.SetColLabelValue( 11, u"Pekerjaan Ibu" )
		self.m_grid1.SetColLabelValue( 12, u"Penghasilan Ibu" )
		self.m_grid1.SetColLabelValue( 13, u"No. Telpon Orang Tua" )
		self.m_grid1.SetColLabelValue( 14, u"Alamat Orang Tua" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.SetRowSize( 0, 50 )
		self.m_grid1.AutoSizeRows()
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.m_grid1, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Log Out", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer12.Add( self.m_button10, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer12, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button10.Bind( wx.EVT_BUTTON, self.btn_logoutF4 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_logoutF4( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 547,638 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText84 = wx.StaticText( self, wx.ID_ANY, u"USER :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		gSizer10.Add( self.m_staticText84, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		gSizer10.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"Nama Siswa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )

		gSizer10.Add( self.m_staticText86, 0, wx.ALL, 5 )

		self.m_textCtrl37 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl37, 0, wx.ALL, 5 )

		self.m_staticText87 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )

		gSizer10.Add( self.m_staticText87, 0, wx.ALL, 5 )

		self.m_textCtrl38 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl38, 0, wx.ALL, 5 )

		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, u"NIK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		gSizer10.Add( self.m_staticText88, 0, wx.ALL, 5 )

		self.m_textCtrl39 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl39, 0, wx.ALL, 5 )

		self.m_staticText89 = wx.StaticText( self, wx.ID_ANY, u"No. Telpon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )

		gSizer10.Add( self.m_staticText89, 0, wx.ALL, 5 )

		self.m_textCtrl40 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl40, 0, wx.ALL, 5 )

		self.m_staticText90 = wx.StaticText( self, wx.ID_ANY, u"Agama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		gSizer10.Add( self.m_staticText90, 0, wx.ALL, 5 )

		m_choice25Choices = [ u"ISLAM", u"BUDHA", u"KONGHUCU", u"HINDU", u"KRISTEN", u"KATOLIK" ]
		self.m_choice25 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice25Choices, 0 )
		self.m_choice25.SetSelection( 3 )
		gSizer10.Add( self.m_choice25, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		gSizer10.Add( self.m_staticText91, 0, wx.ALL, 5 )

		m_choice26Choices = [ u"PRIA", u"WANITA" ]
		self.m_choice26 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice26Choices, 0 )
		self.m_choice26.SetSelection( 1 )
		gSizer10.Add( self.m_choice26, 0, wx.ALL, 5 )

		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		gSizer10.Add( self.m_staticText92, 0, wx.ALL, 5 )

		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl41, 0, wx.ALL, 5 )

		self.m_staticText93 = wx.StaticText( self, wx.ID_ANY, u"Nama Ayah Kandung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		gSizer10.Add( self.m_staticText93, 0, wx.ALL, 5 )

		self.m_textCtrl42 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl42, 0, wx.ALL, 5 )

		self.m_staticText94 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )

		gSizer10.Add( self.m_staticText94, 0, wx.ALL, 5 )

		m_choice27Choices = [ u"PNS", u"SWASTA", u"LAINNYA" ]
		self.m_choice27 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice27Choices, 0 )
		self.m_choice27.SetSelection( 0 )
		gSizer10.Add( self.m_choice27, 0, wx.ALL, 5 )

		self.m_staticText95 = wx.StaticText( self, wx.ID_ANY, u"Penghasilan Ayah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )

		gSizer10.Add( self.m_staticText95, 0, wx.ALL, 5 )

		m_choice28Choices = [ u"<1.000.000", u"1.500.000 - 3.000.000", u"> 3.000.000" ]
		self.m_choice28 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice28Choices, 0 )
		self.m_choice28.SetSelection( 0 )
		gSizer10.Add( self.m_choice28, 0, wx.ALL, 5 )

		self.m_staticText96 = wx.StaticText( self, wx.ID_ANY, u"Nama Ibu Kandung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )

		gSizer10.Add( self.m_staticText96, 0, wx.ALL, 5 )

		self.m_textCtrl43 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl43, 0, wx.ALL, 5 )

		self.m_staticText97 = wx.StaticText( self, wx.ID_ANY, u"Pekerjaan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )

		gSizer10.Add( self.m_staticText97, 0, wx.ALL, 5 )

		m_choice29Choices = [ u"PNS", u"SWASTA", u"LAINNYA", wx.EmptyString ]
		self.m_choice29 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice29Choices, 0 )
		self.m_choice29.SetSelection( 0 )
		gSizer10.Add( self.m_choice29, 0, wx.ALL, 5 )

		self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"Penghasilan Ibu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		gSizer10.Add( self.m_staticText98, 0, wx.ALL, 5 )

		m_choice30Choices = [ u"<1.000.000", u"1.500.000 - 3.000.000", u"> 3.000.000" ]
		self.m_choice30 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice30Choices, 0 )
		self.m_choice30.SetSelection( 0 )
		gSizer10.Add( self.m_choice30, 0, wx.ALL, 5 )

		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"No.Telpon Orang Tua", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		gSizer10.Add( self.m_staticText99, 0, wx.ALL, 5 )

		self.m_textCtrl44 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl44, 0, wx.ALL, 5 )

		self.m_staticText100 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )

		gSizer10.Add( self.m_staticText100, 0, wx.ALL, 5 )

		self.m_textCtrl45 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gSizer10.Add( self.m_textCtrl45, 0, wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Simpan Perubahan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button10, 0, wx.ALL, 5 )


		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



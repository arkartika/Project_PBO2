from wx.core import Frame
import noname
import wx
import mysql.connector

class DataManager:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="pendaftaransiswa")
        self.cursor = self.conn.cursor()

    def Jalankan(self, query, returnData = False):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.conn.commit()
        if returnData :
            return result

class Frame1 (DataManager, noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        self.DM = DataManager()
    def btn_admin( self, event ):
        event = Dialog1(None)
        event.Show()
    def btn_siswa( self, event ):
        event = Dialog1(None)
        event.Show()

class Dialog1 (DataManager, noname.MyDialog1):
    def __init__(self, parent):
        noname.MyDialog1.__init__(self, parent)
        self.DM = DataManager()
    
    def btn_login( self, event ):
        username = self.m_textCtrl1.GetValue()
        password = self.m_textCtrl2.GetValue()

        self.query = "SELECT * FROM akunsiswa WHERE username = '{}' and password = '{}'".format(username, password)
        hasil = self.DM.Jalankan(self.query, returnData = True)
        self.query1 = "SELECT * FROM admin WHERE username = '{}' and password = '{}'".format(username, password)
        hasil1 = self.DM.Jalankan(self.query1, returnData = True)

        if hasil is not None and len(hasil) > 0:
            event = noname.MyFrame3(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        elif hasil1 is not None and len(hasil1) > 0:
            event = noname.MyFrame4(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Username atau Password yang anda masukkan salah', 'Terjadi Kesalahan')
    
run = wx.App()
frame = Frame1(parent=None)
frame.Show()
run.MainLoop()
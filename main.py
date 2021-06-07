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

run = wx.App()
frame = Frame1(parent=None)
frame.Show()
run.MainLoop()
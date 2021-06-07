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
            event = Frame3(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        elif hasil1 is not None and len(hasil1) > 0:
            event = Frame4(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Username atau Password yang anda masukkan salah', 'Terjadi Kesalahan')


class Frame3 (DataManager, noname.MyFrame3):
    def __init__(self, parent):
        noname.MyFrame3.__init__(self, parent)
        self.DM = DataManager()
        self.parent = parent
    def SubmitFrame3( self, event ):
        Nama = self.m_textCtrl3.GetValue()
        Tgl = self.m_textCtrl111.GetValue()
        NIK = self.m_textCtrl6.GetValue()
        Notelp = self.m_textCtrl7.GetValue()
        Agama = self.m_choice2.GetString(self.m_choice2.GetSelection())
        Jenis = self.m_choice3.GetString(self.m_choice3.GetSelection())
        Alamat = self.m_textCtrl8.GetValue()
        Ayah = self.m_textCtrl9.GetValue()
        PekerjaanAyah = self.m_choice4.GetString(self.m_choice4.GetSelection())
        PenghasilanAyah = self.m_choice5.GetString(self.m_choice5.GetSelection())
        Ibu = self.m_textCtrl11.GetValue()
        PekerjaanIbu = self.m_choice6.GetString(self.m_choice6.GetSelection())
        PenghasilanIbu = self.m_choice7.GetString(self.m_choice7.GetSelection())
        NoTelpOrtu = self.m_textCtrl12.GetValue()
        AlamatOrtu = self.m_textCtrl13.GetValue()


        if Nama != "" and Tgl != "" and NIK != "" and Notelp != "" and Agama != "" and Jenis != "" and Alamat != "" and Ayah != "" and PekerjaanAyah != "" and PenghasilanAyah != "" and Ibu != "" and PekerjaanIbu != "" and PenghasilanIbu != "" and NoTelpOrtu != "" and AlamatOrtu != "":
            print(Nama)
            self.query = "INSERT INTO siswa (Nama, Tgl, NIK, Notelp, Agama, Jenis, Alamat, Ayah, PekerjaanAyah, PenghasilanAyah, Ibu, PekerjaanIbu, PenghasilanIbu, NoTelpOrtu, AlamatOrtu) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            self.value = (Nama, Tgl, NIK, Notelp, Agama, Jenis, Alamat, Ayah, PekerjaanAyah, PenghasilanAyah, Ibu, PekerjaanIbu, PenghasilanIbu, NoTelpOrtu, AlamatOrtu)
            self.DM.cursor.execute(self.query, self.value)
            self.DM.conn.commit()
            wx.MessageBox('Data Berhasil', 'Selamat data berhasil disimpan', wx.OK | wx.ICON_INFORMATION)
            event = Frame1(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()

        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')

# class Dialog6 (DataManager, noname.MyDialog6):
#     def __init__(self, parent):
#         noname.MyDialog6.__init__(self, parent)
#         self.DM = DataManager()
#     def btn_logoutD6( self, event ):
#         self.DM.conn.close()
#         event = Frame1(None)
#         event.Show()
#         self.Destroy()

class Frame4 (DataManager, noname.MyFrame4):
    def __init__(self, parent):
        noname.MyFrame4.__init__(self, parent)
        self.DM = DataManager()
        self.tampilData()

    def tampilData(self):
        self.query = 'SELECT Nama, Tgl, NIK, Notelp, Agama, Jenis, Alamat, Ayah, PekerjaanAyah, PenghasilanAyah, Ibu, PekerjaanIbu, PenghasilanIbu, NoTelpOrtu, AlamatOrtu FROM siswa'
        hasil = self.DM.Jalankan(self.query, returnData=True)
        for a in range (15) :
            b = 0
            for row in hasil:
                self.m_grid1.SetCellValue(b, a, str(row[a]))
                b = b+1

    def btn_logoutF4( self, event ):
        self.DM.conn.close()
        event = Frame1(None)
        event.Show()
        self.Destroy()




run = wx.App()
frame = Frame1(parent=None)
frame.Show()
run.MainLoop()
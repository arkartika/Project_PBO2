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

        self.query = "SELECT * FROM siswa WHERE username = '{}' and password = '{}'".format(username, password)
        hasil = self.DM.Jalankan(self.query, returnData = True)
        self.query1 = "SELECT * FROM admin WHERE username = '{}' and password = '{}'".format(username, password)
        hasil1 = self.DM.Jalankan(self.query1, returnData = True)
        
        if hasil is not None and len(hasil) > 0:
            event = Frame3(None, hasil)
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
    def __init__(self, parent, data):
        noname.MyFrame3.__init__(self, parent)
        self.DM = DataManager()
        self.parent = parent
        self.data = data
        self.m_textCtrl3.write(self.data[0][3])
        self.m_textCtrl111.write(self.data[0][4])
        self.m_textCtrl6.write(self.data[0][5])
        self.m_textCtrl7.write(self.data[0][6])
        self.m_textCtrl8.write(self.data[0][10])
        self.m_textCtrl9.write(self.data[0][11])
        self.m_textCtrl11.write(self.data[0][14])
        self.m_textCtrl12.write(self.data[0][17])
        self.m_textCtrl13.write(self.data[0][18])

        if self.data [0][7] == "ISLAM":
            self.m_choice2.SetSelection(0)
        elif self.data [0][7] == "BUDHA":
            self.m_choice2.SetSelection(1)
        elif self.data [0][7] == "KONGHUCHU":
            self.m_choice2.SetSelection(2)
        elif self.data [0][7] == "HINDU":
            self.m_choice2.SetSelection(3)
        elif self.data [0][7] == "KRISTEN":
            self.m_choice2.SetSelection(4)
        elif self.data [0][7] == "KATOLIK":
            self.m_choice2.SetSelection(5)

        if self.data [0][8] == "PRIA":
            self.m_choice3.SetSelection(0)
        elif self.data [0][8] == "WANITA":
            self.m_choice3.SetSelection(1)
        
        if self.data [0][9] == "< 1 km":
            self.m_choice71.SetSelection(0)
        elif self.data [0][9] == "1 km - 5 km":
            self.m_choice71.SetSelection(1)
        elif self.data [0][9] == "> 5 km":
            self.m_choice71.SetSelection(2)

        if self.data [0][11] == "PNS":
            self.m_choice4.SetSelection(0)
        elif self.data [0][11] == "SWASTA":
            self.m_choice4.SetSelection(1)
        elif self.data [0][11] == "LAINNYA":
            self.m_choice4.SetSelection(2)

        if self.data [0][12] == "<1.000.000":
            self.m_choice5.SetSelection(0)
        elif self.data [0][12] == "1.500.000 - 3.000.000":
            self.m_choice5.SetSelection(1)
        elif self.data [0][12] == ">3.000.000":
            self.m_choice5.SetSelection(2)

        if self.data [0][14] == "PNS":
            self.m_choice6.SetSelection(0)
        elif self.data [0][14] == "SWASTA":
            self.m_choice6.SetSelection(1)
        elif self.data [0][14] == "LAINNYA":
            self.m_choice6.SetSelection(2)

        if self.data [0][15] == "<1.000.000":
            self.m_choice7.SetSelection(0)
        elif self.data [0][15] == "1.500.000 - 3.000.000":
            self.m_choice7.SetSelection(1)
        elif self.data [0][15] == ">3.000.000":
            self.m_choice7.SetSelection(2)

    def SubmitFrame3( self, event ):
        Nama = self.m_textCtrl3.GetValue()
        Tgl = self.m_textCtrl111.GetValue()
        NIK = self.m_textCtrl6.GetValue()
        Notelp = self.m_textCtrl7.GetValue()
        Agama = self.m_choice2.GetString(self.m_choice2.GetSelection())
        Jenis = self.m_choice3.GetString(self.m_choice3.GetSelection())
        Jarak = self.m_choice71.GetString(self.m_choice71.GetSelection())
        Alamat = self.m_textCtrl8.GetValue()
        Ayah = self.m_textCtrl9.GetValue()
        PekerjaanAyah = self.m_choice4.GetString(self.m_choice4.GetSelection())
        PenghasilanAyah = self.m_choice5.GetString(self.m_choice5.GetSelection())
        Ibu = self.m_textCtrl11.GetValue()
        PekerjaanIbu = self.m_choice6.GetString(self.m_choice6.GetSelection())
        PenghasilanIbu = self.m_choice7.GetString(self.m_choice7.GetSelection())
        NoTelpOrtu = self.m_textCtrl12.GetValue()
        AlamatOrtu = self.m_textCtrl13.GetValue()

        if Nama != "" and Tgl != "" and NIK != "" and Notelp != "" and Agama != "" and Jenis != "" and Jarak != "" and Alamat != "" and Ayah != "" and PekerjaanAyah != "" and PenghasilanAyah != "" and Ibu != "" and PekerjaanIbu != "" and PenghasilanIbu != "" and NoTelpOrtu != "" and AlamatOrtu != "":
            print(Nama)
            self.query = "update siswa set Nama = %s, Tgl = %s, NIK = %s, Notelp = %s, Agama = %s, Jenis = %s, Jarak = %s, Alamat = %s, Ayah = %s, PekerjaanAyah = %s, PenghasilanAyah = %s, Ibu = %s, PekerjaanIbu = %s, PenghasilanIbu =%s, NoTelpOrtu = %s, AlamatOrtu = %s WHERE id = %s"
            self.value = (Nama, Tgl, NIK, Notelp, Agama, Jenis, Jarak, Alamat, Ayah, PekerjaanAyah, PenghasilanAyah, Ibu, PekerjaanIbu, PenghasilanIbu, NoTelpOrtu, AlamatOrtu, self.data[0][0])
            self.DM.cursor.execute(self.query, self.value)
            self.DM.conn.commit()
            wx.MessageBox('Data Berhasil', 'Selamat data berhasil disimpan', wx.OK | wx.ICON_INFORMATION)
            event = Frame1(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')

class Frame4 (DataManager, noname.MyFrame4):
    def __init__(self, parent):
        noname.MyFrame4.__init__(self, parent)
        self.DM = DataManager()
        self.tampilData()

    def tampilData(self):
        self.query = 'SELECT Nama, Tgl, NIK, Notelp, Agama, Jenis, Jarak, Alamat, Ayah, PekerjaanAyah, PenghasilanAyah, Ibu, PekerjaanIbu, PenghasilanIbu, NoTelpOrtu, AlamatOrtu FROM siswa'
        hasil = self.DM.Jalankan(self.query, returnData=True)
        for a in range (16) :
            b = 0
            for row in hasil:
                self.m_grid1.SetCellValue(b, a, str(row[a]))
                b = b+1

    def btn_logoutF4( self, event ):
        self.DM.conn.close()
        event = Frame1(None)
        event.Show()
        self.Destroy()
    
    def btn_Akun(self, event):
        event = Dialog3(None)
        event.Show()
        # self.Destroy()
        self.DM.conn.close()

class Dialog3 (DataManager, noname.MyDialog3):
    def __init__(self, parent):
        noname.MyDialog3.__init__(self,parent)
        self.DM = DataManager()
        
    def btn_daftar(self, event):
        Username = self.m_textCtrl46.GetValue()
        Password = self.m_textCtrl47.GetValue()

        if Username != "" and Password != "":
            self.query = "INSERT INTO siswa (Username, Password) VALUES (%s , %s)"
            self.value = (Username, Password)
            self.DM.cursor.execute(self.query, self.value)
            self.DM.conn.commit()
            wx.MessageBox('Data Berhasil', 'Selamat data berhasil disimpan', wx.OK | wx.ICON_INFORMATION)
            event = Frame1(None)
            event.Show()
            self.Destroy()
            self.DM.conn.close()
        else:
            wx.MessageBox('Data tidak boleh kosong', 'Terjadi Kesalahan')
            
run = wx.App()
frame = Frame1(parent=None)
frame.Show()
run.MainLoop()
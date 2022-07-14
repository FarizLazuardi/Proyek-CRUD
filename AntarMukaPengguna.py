from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from TelefonDefteriGUI import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global id, Nama, Marga, Kota, Telepon, Email


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.btnDaftarClick()
        self.ui.btnDaftar.clicked.connect(self.btnDaftarClick)
        self.ui.btnSimpan.clicked.connect(self.btnSimpanClick)
        self.ui.btnHapus.clicked.connect(self.btnHapusClick)
        self.ui.btnPerbarui.clicked.connect(self.btnPerbaruiClick)
        self.ui.tblDaftar.clicked.connect(self.DaftarOnClick) 
 
    def btnHapus(self):
        self.ui.txtID.clear()
        self.ui.txtNama.clear()
        self.ui.txtNama.clear()
        self.ui.txtKota.clear()
        self.ui.txtTelepon.clear()
        self.ui.txtEmail.clear()

    def DaftarOnClick(self): 
        self.ui.txtID.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 0).text())
        self.ui.txtNama.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 1).text())
        self.ui.txtMarga.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 2).text())
        self.ui.txtKota.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 3).text())
        self.ui.txtTelepon.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 4).text())
        self.ui.txtEmail.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 5).text())
 
    def btnSimpanClick(self): 
        id = self.ui.txtID.text()
        Nama = self.ui.txtNama.text()
        Marga = self.ui.txtMarga.text()
        Kota = self.ui.txtKota.text()
        Telepon = self.ui.txtTelepon.text()
        Email = self.ui.txtEmail.text()

#"CREATE TABLE PENGGUNA (id INT, Nama TEXT, Marga TEXT, Kota TEXT, Telepon TEXT, Email TEXT)"

        try:
            self.conn = sql.connect("BukuTelepon.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO PENGGUNA VALUES (?,?,?,?,?,?)",(id,Nama,Marga,Kota,Telepon,Email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.btnHapus()
        self.btnDaftarClick()

    def btnDaftarClick(self):  
        self.ui.tblDaftar.clear()
        self.ui.tblDaftar.setColumnCount(6)
        self.ui.tblDaftar.setHorizontalHeaderLabels(('id','Nama','Marga','Kota','Telepon','Email'))
        self.ui.tblDaftar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('BukuTelepon.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM PENGGUNA"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tblDaftar.setRowCount(len(rows))
        
        for BarisIndeks, BarisData in enumerate(rows):
            for KolomIndeks, KolomData in enumerate (BarisData):
                self.ui.tblDaftar.setItem(BarisIndeks,KolomIndeks,QTableWidgetItem(str(KolomData))) 
    
    def btnPerbaruiClick(self):  
        id = self.ui.txtID.text()
        Nama = self.ui.txtNama.text()
        Marga = self.ui.txtMarga.text()
        Kota = self.ui.txtKota.text()
        Telepon = self.ui.txtTelepon.text()
        Email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("BukuTelepon.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE PENGGUNA SET Nama = ?, Marga = ?, Kota = ?, \
                Telepon = ?, Email = ? WHERE id = ?",(Nama,Marga,Kota,Telepon,Email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.btnHapus()
        self.btnDaftarClick()

    def btnHapusClick(self): 
        id = self.ui.txtID.text() 

        try:
            self.conn = sql.connect("BukuTelepon.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM PENGGUNA WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.btnHapus()
        self.btnDaftarClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelefonDefteriGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSimpan = QtWidgets.QPushButton(self.centralwidget)
        self.btnSimpan.setGeometry(QtCore.QRect(560, 20, 211, 41))
        self.btnSimpan.setObjectName("btnSimpan")
        self.btnHapus = QtWidgets.QPushButton(self.centralwidget)
        self.btnHapus.setGeometry(QtCore.QRect(560, 70, 211, 41))
        self.btnHapus.setObjectName("btnHapus")
        self.btnPerbarui = QtWidgets.QPushButton(self.centralwidget)
        self.btnPerbarui.setGeometry(QtCore.QRect(560, 120, 211, 41))
        self.btnPerbarui.setObjectName("btnPerbarui")
        self.btnDaftar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDaftar.setGeometry(QtCore.QRect(560, 170, 211, 41))
        self.btnDaftar.setObjectName("btnDaftar")
        self.txtID = QtWidgets.QLineEdit(self.centralwidget)
        self.txtID.setGeometry(QtCore.QRect(220, 20, 311, 41))
        self.txtID.setObjectName("txtID")
        self.txtNama = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNama.setGeometry(QtCore.QRect(220, 70, 311, 41))
        self.txtNama.setObjectName("txtNama")
        self.txtMarga = QtWidgets.QLineEdit(self.centralwidget)
        self.txtMarga.setGeometry(QtCore.QRect(220, 120, 311, 41))
        self.txtMarga.setObjectName("txtMarga")
        self.txtKota = QtWidgets.QLineEdit(self.centralwidget)
        self.txtKota.setGeometry(QtCore.QRect(220, 170, 311, 41))
        self.txtKota.setObjectName("txtKota")
        self.txtTelepon = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelepon.setGeometry(QtCore.QRect(220, 220, 311, 41))
        self.txtTelepon.setObjectName("txtTelefon")
        self.txtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.txtEmail.setGeometry(QtCore.QRect(220, 270, 311, 41))
        self.txtEmail.setObjectName("txtEmail")
        self.lblID = QtWidgets.QLabel(self.centralwidget)
        self.lblID.setGeometry(QtCore.QRect(10, 20, 201, 41))
        self.lblID.setObjectName("lblID")
        self.lblNama = QtWidgets.QLabel(self.centralwidget)
        self.lblNama.setGeometry(QtCore.QRect(10, 70, 201, 41))
        self.lblNama.setObjectName("lblNama")
        self.lblMarga = QtWidgets.QLabel(self.centralwidget)
        self.lblMarga.setGeometry(QtCore.QRect(10, 120, 201, 41))
        self.lblMarga.setObjectName("lblMarga")
        self.lblKota = QtWidgets.QLabel(self.centralwidget)
        self.lblKota.setGeometry(QtCore.QRect(10, 170, 201, 41))
        self.lblKota.setObjectName("lblKota")
        self.lblTelepon = QtWidgets.QLabel(self.centralwidget)
        self.lblTelepon.setGeometry(QtCore.QRect(10, 220, 201, 41))
        self.lblTelepon.setObjectName("lblTelepon")
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(10, 270, 201, 41))
        self.lblEmail.setObjectName("lblEmail")
        self.tblDaftar = QtWidgets.QTableWidget(self.centralwidget)
        self.tblDaftar.setGeometry(QtCore.QRect(10, 330, 891, 341))
        self.tblDaftar.setObjectName("tblDaftar")
        self.tblDaftar.setColumnCount(0)
        self.tblDaftar.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSimpan.setText(_translate("MainWindow", "Simpan"))
        self.btnHapus.setText(_translate("MainWindow", "Hapus"))
        self.btnPerbarui.setText(_translate("MainWindow", "Perbarui"))
        self.btnDaftar.setText(_translate("MainWindow", "Daftar"))
        self.lblID.setText(_translate("MainWindow", "ID"))
        self.lblNama.setText(_translate("MainWindow", "Nama"))
        self.lblMarga.setText(_translate("MainWindow", "Marga"))
        self.lblKota.setText(_translate("MainWindow", "Kota"))
        self.lblTelepon.setText(_translate("MainWindow", "Telepon"))
        self.lblEmail.setText(_translate("MainWindow", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
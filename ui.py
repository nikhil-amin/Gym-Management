# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crud.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

import sqlite3

class Ui_MainWindow(object):

    #######################################################################################
    def display(self):
        connection = sqlite3.connect('gymDB.db')
        query = "SELECT * FROM gymmembers"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def fill_details(self):
        if self.tableWidget.currentIndex().row() > -1:
            row = self.tableWidget.currentIndex().row()
            memberID = self.tableWidget.item(row,0).text()
            name = self.tableWidget.item(row,1).text()
            address = self.tableWidget.item(row,2).text()
            contact = self.tableWidget.item(row,3).text()
            email = self.tableWidget.item(row,4).text()

            self.lineEdit_name.setText(name)
            self.lineEdit_address.setText(address)
            self.lineEdit_contact.setText(contact)
            self.lineEdit_email.setText(email)

    def add(self):
        connection = sqlite3.connect('gymDB.db')
        name = self.lineEdit_name.text()
        address = self.lineEdit_address.text()
        contact = self.lineEdit_contact.text()
        email = self.lineEdit_email.text()

        cur = connection.cursor()
        cur.execute('''INSERT INTO gymmembers(name, address, contact, email) VALUES(?,?,?,?)''', (name, address, contact, email))
        
        connection.commit()
        connection.close()

    def delete(self):
        connection = sqlite3.connect('gymDB.db')

        if self.tableWidget.currentIndex().row() > -1:
            row = self.tableWidget.currentIndex().row()
            memberID = self.tableWidget.item(row,0).text()
            name = self.tableWidget.item(row,1).text()
            address = self.tableWidget.item(row,2).text()
            contact = self.tableWidget.item(row,3).text()
            email = self.tableWidget.item(row,4).text()

            self.lineEdit_name.setText(name)
            self.lineEdit_address.setText(address)
            self.lineEdit_contact.setText(contact)
            self.lineEdit_email.setText(email)
        
        cur = connection.cursor()
        query = "DELETE FROM gymmembers WHERE memberID = {}".format(memberID)
        
        try: 
            cur.execute(query)          
            connection.commit()
        except:
            print(sys.exc_info())
            cur.rollback()

    def update(self):
        connection = sqlite3.connect('gymDB.db')

        if self.tableWidget.currentIndex().row() > -1:
            row = self.tableWidget.currentIndex().row()
            memberID = self.tableWidget.item(row,0).text()
         

    
            name=self.lineEdit_name.text()
            address=self.lineEdit_address.text()
            contact=self.lineEdit_contact.text()
            email=self.lineEdit_email.text()

            self.lineEdit_name.setText(name)
            self.lineEdit_address.setText(address)
            self.lineEdit_contact.setText(contact)
            self.lineEdit_email.setText(email)

        cur = connection.cursor()
        query="UPDATE gymmembers SET name = '{}', address ='{}', contact = '{}', email = '{}' WHERE memberID = {}".format(name, address, contact, email, memberID)
        try:
            cur.execute(query)
            connection.commit()
            
        except:
            print(sys.exc_info())
            cur.rollback()

    def clear(self):
        self.lineEdit_name.setText('')
        self.lineEdit_address.setText('')
        self.lineEdit_contact.setText('')
        self.lineEdit_email.setText('')
 
    #######################################################################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(30, 390, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(190, 390, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(110, 390, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_update.setFont(font)
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(270, 390, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")

        #######################################################################################
        self.pushButton_clear.clicked.connect(self.clear)

        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_add.clicked.connect(self.display)
        self.pushButton_add.clicked.connect(self.clear)

        self.pushButton_update.clicked.connect(self.update)
        self.pushButton_update.clicked.connect(self.display)
        self.pushButton_update.clicked.connect(self.clear)

        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_delete.clicked.connect(self.display)
        self.pushButton_delete.clicked.connect(self.clear)

        #######################################################################################

        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(162, 110, 181, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_controlpanel = QtWidgets.QLabel(self.centralwidget)
        self.label_controlpanel.setGeometry(QtCore.QRect(110, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_controlpanel.setFont(font)
        self.label_controlpanel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_controlpanel.setObjectName("label_controlpanel")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(40, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_name.setObjectName("label_name")
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(160, 170, 181, 31))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.label_address = QtWidgets.QLabel(self.centralwidget)
        self.label_address.setGeometry(QtCore.QRect(38, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_address.setFont(font)
        self.label_address.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_address.setObjectName("label_address")
        self.lineEdit_contact = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contact.setGeometry(QtCore.QRect(162, 230, 181, 31))
        self.lineEdit_contact.setObjectName("lineEdit_contact")
        self.label_contact = QtWidgets.QLabel(self.centralwidget)
        self.label_contact.setGeometry(QtCore.QRect(40, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_contact.setFont(font)
        self.label_contact.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_contact.setObjectName("label_contact")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(162, 290, 181, 31))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(40, 290, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_email.setFont(font)
        self.label_email.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_email.setObjectName("label_email")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(370, 40, 321, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.itemClicked.connect(self.fill_details)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gym Management System"))
        self.pushButton_add.setText(_translate("MainWindow", "ADD"))
        self.pushButton_delete.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_update.setText(_translate("MainWindow", "UPDATE"))
        self.pushButton_clear.setText(_translate("MainWindow", "CLEAR"))
        self.label_controlpanel.setText(_translate("MainWindow", "Control Panel"))
        self.label_name.setText(_translate("MainWindow", "Name:"))
        self.label_address.setText(_translate("MainWindow", "Address:"))
        self.label_contact.setText(_translate("MainWindow", "Contact:"))
        self.label_email.setText(_translate("MainWindow", "Email ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


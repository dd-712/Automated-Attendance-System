# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\sem7\Minor Project\UI\deepface\UI Files\studentclasscameragui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background-color: rgb(219, 221, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 250, 141, 31))
        self.label.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 300, 141, 31))
        self.label_2.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_2.setObjectName("label_2")
        self.rollno = QtWidgets.QLabel(self.centralwidget)
        self.rollno.setGeometry(QtCore.QRect(610, 250, 281, 31))
        self.rollno.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.rollno.setObjectName("rollno")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(610, 300, 281, 31))
        self.name.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 30, 471, 41))
        self.label_3.setStyleSheet("color: rgb(60, 25, 255);\n"
"font: 16pt \"Nirmala UI\";")
        self.label_3.setObjectName("label_3")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(610, 200, 281, 31))
        self.name_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.name_2.setObjectName("name_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 200, 141, 31))
        self.label_4.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 150, 141, 31))
        self.label_5.setStyleSheet("color: rgb(0, 85, 127);\n"
"font: 14pt \"Nirmala UI\";")
        self.label_5.setObjectName("label_5")
        self.rollno_2 = QtWidgets.QLabel(self.centralwidget)
        self.rollno_2.setGeometry(QtCore.QRect(610, 150, 281, 31))
        self.rollno_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.rollno_2.setObjectName("rollno_2")
        self.leave = QtWidgets.QPushButton(self.centralwidget)
        self.leave.setGeometry(QtCore.QRect(510, 380, 161, 31))
        self.leave.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(52, 168, 83);")
        self.leave.setObjectName("leave")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Course ID</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Faculty ID</p></body></html>"))
        self.rollno.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">course id</span></p></body></html>"))
        self.name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Faculty</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Class is Going On Your Face is Recorded</span></p></body></html>"))
        self.name_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Date</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Date</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Roll No</span></p></body></html>"))
        self.rollno_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Roll No</span></p></body></html>"))
        self.leave.setText(_translate("MainWindow", "Leave Meeting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
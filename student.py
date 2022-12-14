from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from studentloginfirstgui import Ui_MainWindow
import sqlite3
import popupcode
import studentCamera
import studentreport
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, roll_n, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.roll_no = roll_n
        self.title.setText('Hello ' + self.roll_no)
        # print('done')
        try:
            self.set_class.clicked.connect(self.openJoin)
        except Exception as e:
            print(e)
        self.Check_Students.clicked.connect(self.studentCheck)
        self.run()

    def openJoin(self):
        roll_no = self.roll_no
        # print(roll_no)
        # print(self.course_id.toPlainText())
        course_id = self.course_id.toPlainText()
        faculty_id = self.faculty_id.toPlainText()
        # print(datetime.datetime.now().date())
        datee = datetime.datetime.now().date()
        # print(datee)
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT * FROM CLASSES WHERE date=(?) AND faculty_id=(?)", (datee, faculty_id))
        result = cursor.fetchall()

        if len(result) == 0:
            self.popup = popupcode.MainWindow()
        else:
            cursor = conn.execute("SELECT * FROM STUDIES WHERE roll_no=(?) AND faculty_id=(?)", (roll_no, faculty_id))
            result = cursor.fetchall()
            # print(result)
            if len(result) == 0:
                self.popup = popupcode.MainWindow()
            else:
                self.studentCameraWindow = studentCamera.MainWindow(roll_no, faculty_id, course_id, datee)

        conn.close()

    def studentCheck(self):
        self.studentreport = studentreport.MainWindow(self.roll_no)

    def run(self):
        self.show()

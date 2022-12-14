import datetime

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from teacherlogingui import Ui_MainWindow
import sqlite3
import teacherCheckReport
from datetime import date


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, faculty_id, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.faculty_id=faculty_id
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursor = conn.execute("SELECT FFNAME,FLNAME FROM TEACHER WHERE faculty_id=(?)", (faculty_id, ))
        result = cursor.fetchall()
        self.title.setText('Hello '+result[0][0]+' '+result[0][1])
        self.set_class.clicked.connect(self.setClass)
        self.Check_Students.clicked.connect(self.Check_Student)
        conn.close()
        self.run()

    def Check_Student(self):
        self.check_student = teacherCheckReport.MainWindow(self.faculty_id)

    def setClass(self):
        # print(self.date.toPlainText())
        try:
            Entered_Date = datetime.datetime.strptime(self.date.toPlainText(), '%Y-%m-%d').date()
        except Exception as e:
            self.error.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; '
                               'color:#aa0000;">Enter Valid Date</span></p></body></html>')
            return
        today=datetime.datetime.now().date()
        # print(Entered_Date+' '+today)
        # print(Entered_Date)
        # print(today)
        if Entered_Date<today:
            self.error.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; '
                               'color:#aa0000;">Enter Valid Date</span></p></body></html>')
        else:
            conn = sqlite3.connect('attendance.db')
            conn.execute('PRAGMA foreign_keys=on;')
            cursorexe = conn.cursor()
            cursorexe.execute("INSERT INTO CLASSES VALUES (?,?)",
                              (Entered_Date, self.faculty_id))
            conn.commit()
            conn.close()
            self.error.setText('<html><head/><body><p align="center"><span style=" font-size:14pt; '
                               'color:#aa0000;">Class Set Successfully!!!</span></p></body></html>')
    def run(self):
        self.show()

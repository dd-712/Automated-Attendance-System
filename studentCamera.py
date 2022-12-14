from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from studentclasscameragui import Ui_MainWindow
import sqlite3
from emotion import emotionIdentify
from face import faceRecognize
import database
import sqlite3
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, roll_no, faculty_id, course_id, datee, *args, **kwargs):
        # print(roll_no, faculty_id,course_id, datee)
        try:
            super(MainWindow, self).__init__(*args, **kwargs)
        except Exception as e:
            print(e)

        self.setupUi(self)
        self.rollno_2.setText(roll_no)
        self.name_2.setText(datee.strftime("%d/%m/%Y"))
        self.rollno.setText(course_id)
        self.name.setText(faculty_id)

        fr = faceRecognize()
        roll_no = fr.recognize()
        # print(roll_no)

        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        cursorexe = conn.cursor()
        
        self.run()

        ei = emotionIdentify()
        emot = ei.identifyEmotion()
        # print(emot)

        try:
            cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?,?,?,?,?,?)",
                     (roll_no, datee, 'P', course_id, faculty_id, float("{:.2f}".format((emot['yes']*100)/(emot['yes']+emot['not'])))))
        except Exception as e:
            print(e)
        conn.commit()

        conn.close()

        self.leave.clicked.connect(self.terminate)
        

    def terminate(self):
        self.close()

    def run(self):
        self.show()

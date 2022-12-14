from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from teacherstudentreportgui import Ui_MainWindow
import sqlite3
import popupcode
import datetime


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, faculty_id, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        total_classes = list(conn.execute("SELECT count(*) FROM CLASSES "
                                          "WHERE faculty_id=(?)",
                                          (faculty_id,)))
        total_classes = total_classes[0][0]
        tot_student = 0
        tot_attendance = 0
        tot_attention = 0

        students = list(conn.execute("SELECT roll_no FROM STUDIES "
                                     "WHERE faculty_id=(?)",
                                     (faculty_id,)))
        row1 = list()
        for student in students:
            tot_student+=1
            roll_no = student[0]
            name = list(conn.execute("SELECT SFNAME,SLNAME FROM STUDENT "
                                     "WHERE roll_no=(?)",
                                     (roll_no,)))
            name=name[0][0]+' '+name[0][1]
            # Attended_classes = list(
            #     conn.execute("SELECT count(*) FROM ATTENDANCE WHERE roll_no=(?) AND faculty_id=(?)"
            #                  , (roll_no, faculty_id,)))
            Attention=list(conn.execute("SELECT attention_status FROM ATTENDANCE WHERE roll_no=(?) AND faculty_id=(?)",(roll_no, faculty_id,)))
            attention_per=0
            percentage=0
            for val in Attention:
                attention_per=attention_per+val[0]
            if len(Attention)!=0:
                attention_per=attention_per/len(Attention)
            
            Attended_classes = len(Attention)
            if total_classes==0:
                percentage=100
            else:
                percentage = Attended_classes * 100 / total_classes
            tot_attendance=tot_attendance+percentage
            tot_attention=tot_attention+attention_per

            percentage = "{:.2f}%".format(percentage)
            attention_per= "{:.2f}%".format(attention_per)
            row1.append([name,roll_no,percentage,attention_per])
            conn.commit()

        for row1x in row1:
            tableRowNumber = self.sheet.rowCount()
            self.sheet.setRowCount(tableRowNumber + 1)
            col = 0
            for item in row1x:
                cell = QTableWidgetItem(str(item))
                self.sheet.setItem(tableRowNumber, col, cell)
                col =col+ 1
        # print(tot_student)
        # print(tot_attendance)
        if tot_student==0:
            tot_student=tot_attendance=1
        # print(tot_attendance+' '+tot_student)
        percentage=tot_attendance/tot_student
        attention_per=tot_attention/tot_student
        # print(percentage)
        percentage = "{:.2f}%".format(percentage)
        attention_per = "{:.2f}%".format(attention_per)
        self.attendance.setText(percentage)
        self.attention.setText(attention_per)
        conn.close()
        self.run()

    def run(self):
        self.show()

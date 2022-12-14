from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from studentlogingui import Ui_MainWindow
import sqlite3
import popupcode


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, roll_no, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.studentDisplay(roll_no)
        self.run()

    def run(self):
        self.show()

    def studentDisplay(self, roll_no):
        conn = sqlite3.connect('attendance.db')
        conn.execute('PRAGMA foreign_keys=on;')
        name = list(conn.execute("SELECT SFNAME,SLNAME FROM STUDENT WHERE roll_no=(?)", (roll_no,)))
        self.rollno.setText(roll_no)
        self.name.setText(name[0][0] + " " + name[0][1])
        cursor = conn.execute("SELECT * FROM ATTENDANCE WHERE roll_no=(?)", (roll_no,))
        result = cursor.fetchall()
        if len(result) == 0:
            hello = 1
        else:
            self.run()
            course_id = set(conn.execute("SELECT course_id, faculty_id FROM STUDIES WHERE roll_no=(?)", (roll_no,)))
            course_id = list(course_id)
            course_id.sort()
            row1 = list()
            for subjects in course_id:
                total_classes = list(conn.execute("SELECT count(*) FROM CLASSES INNER JOIN STUDIES ON "
                                                  "CLASSES.faculty_id=STUDIES.faculty_id "
                                                  "WHERE STUDIES.roll_no=(?) AND STUDIES.course_id=(?)",
                                                  (roll_no, subjects[0],)))
                total_classes = total_classes[0][0]
                print(total_classes,subjects)
                Attended_classes = list(
                    conn.execute("SELECT count(*) FROM ATTENDANCE WHERE roll_no=(?) AND course_id=(?) "
                                 , (roll_no, subjects[0],)))
                Attended_classes = Attended_classes[0][0]
                if total_classes == 0:
                    continue
                percentage = Attended_classes * 100 / total_classes
                row = list(conn.execute("SELECT * FROM (SELECT * FROM ATTENDANCE INNER JOIN COURSE ON "
                                        "ATTENDANCE.course_id=COURSE.course_id WHERE roll_no=(?)) WHERE course_id=(?)",
                                        (roll_no, subjects[0],)))
                if len(row)==0:
                    course_name=list(conn.execute("Select course_name FROM COURSE WHERE course_id=(?)",(subjects[0],)))
                    row1.append([subjects[0], course_name[0][0], subjects[1], "{:.2f}%".format(0), "{:.2f}%".format(0)])
                    conn.commit()
                    continue

                attention=0
                
                for val in row:
                    attention=attention+val[5]
                attention=attention/len(row)

                percentage = "{:.2f}%".format(percentage)
                attention = "{:.2f}%".format(attention)

                row1.append([subjects[0], row[0][7], row[0][4], percentage, attention])
                conn.commit()

            for row1x in row1:
                tableRowNumber = self.primary.rowCount()
                self.primary.setRowCount(tableRowNumber + 1)
                col = 0
                for item in row1x:
                    cell = QTableWidgetItem(str(item))
                    self.primary.setItem(tableRowNumber, col, cell)
                    col += 1
            rows = list(
                conn.execute("SELECT * FROM ATTENDANCE INNER JOIN COURSE ON "
                             "ATTENDANCE.course_id=COURSE.course_id WHERE roll_no=(?)", (roll_no,)))
            row1.clear()

            faculty_id=list(conn.execute("SELECT faculty_id FROM STUDIES WHERE roll_no=(?)", (roll_no,)))
            lecs=[]

            for fac in faculty_id:
                lec=list(conn.execute("SELECT * FROM CLASSES WHERE faculty_id=(?)",(fac[0])))
                if len(lec)==0:
                    continue
                lecs=lecs+lec
            
            inde=0
            datee=[]
            for row in rows:
                datee.append((row[1],row[4]))
                row1.append([row[3], row[7], row[4], row[1], row[2]])
            
            while inde<len(lecs):
                if lecs[inde] not in datee:
                    cid=list(conn.execute("SELECT course_id FROM TEACHER WHERE faculty_id=(?)",(lecs[inde][1])))
                    cname=list(conn.execute("SELECT course_name FROM COURSE WHERE course_id=(?)",(cid[0])))
                    row1.append([cid[0][0],cname[0][0],lecs[inde][1],lecs[inde][0],'A'])
                inde+=1

            for row1x in row1:
                tableRowNumber = self.secondary.rowCount()
                self.secondary.setRowCount(tableRowNumber + 1)
                col = 0
                for item in row1x:
                    cell = QTableWidgetItem(str(item))
                    self.secondary.setItem(tableRowNumber, col, cell)
                    col += 1
        conn.close()

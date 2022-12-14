import sqlite3
import datetime

conn = sqlite3.connect('attendance.db')
conn.execute('PRAGMA foreign_keys=on;')
cursorexe = conn.cursor()

# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("1","Elon","Musk","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("2","Jeff","Bezos","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("166","Dip","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("167","Divya","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("175","Hrushi","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("176","Jaan","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("187","Neel","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("189","Parthiv","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("193","Raj","Patel","1234"))
# cursorexe.execute("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", ("270","Harshil","Tagadiya","1234"))

# cursorexe.execute("INSERT INTO CLASSES VALUES (?,?)",(datetime.datetime.strptime("2022-01-03",'%Y-%m-%d').date(), "4"))
# cursorexe.execute("INSERT INTO CLASSES VALUES (?,?)",(datetime.datetime.strptime("2022-01-04",'%Y-%m-%d').date(), "4"))
# cursorexe.execute("INSERT INTO CLASSES VALUES (?,?)",(datetime.datetime.strptime("2022-01-05",'%Y-%m-%d').date(), "4"))
# cursorexe.execute("INSERT INTO CLASSES VALUES (?,?)",(datetime.datetime.strptime("2022-01-06",'%Y-%m-%d').date(), "4"))

# for i in [datetime.datetime.strptime("2022-01-03",'%Y-%m-%d').date(),datetime.datetime.strptime("2022-01-04",'%Y-%m-%d').date(),datetime.datetime.strptime("2022-01-05",'%Y-%m-%d').date(),datetime.datetime.strptime("2022-01-06",'%Y-%m-%d').date()]:
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("1",i,"P","2CE1","1",87.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("2",i,"P","2CE1","1",81.2))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("167",i,"P","2CE1","1",90))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("175",i,"P","2CE1","1",72))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("176",i,"P","2CE1","1",81))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("187",i,"P","2CE1","1",87))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("270",i,"P","2CE1","1",81.6))

#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("1",i,"P","2CE2","2",84))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("2",i,"P","2CE2","2",87.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("166",i,"P","2CE2","2",77))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("167",i,"P","2CE2","2",77.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("175",i,"P","2CE2","2",89))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("187",i,"P","2CE2","2",23))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("193",i,"P","2CE2","2",87))

#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("1",i,"P","2CE3","3",87))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("167",i,"P","2CE3","3",87))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("175",i,"P","2CE3","3",82))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("176",i,"P","2CE3","3",72))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("187",i,"P","2CE3","3",87.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("193",i,"P","2CE3","3",762))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("270",i,"P","2CE3","3",12))

#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("1",i,"P","2CE4","4",76))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("2",i,"P","2CE4","4",89))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("167",i,"P","2CE4","4",87.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("175",i,"P","2CE4","4",87.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("176",i,"P","2CE4","4",94))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("189",i,"P","2CE4","4",87.6))
#     cursorexe.execute("INSERT INTO ATTENDANCE VALUES (?, ?, ?, ?, ?, ?)",("193",i,"P","2CE4","4",87.6))

# conn.commit()
# conn.close()
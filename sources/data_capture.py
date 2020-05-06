import sqlite3
from tkinter import messagebox
import sys

TEST_ROW = 0

def get_ip_data(db):
 try:
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    sql = 'select Lesson_Title,IP_Questions, Lesson_ID, NumberOfQuestions from Magic_Science_Lessons where Lesson_ID=?'
    ip_info_c = cur.execute(sql, (TEST_ROW,))
    ip_info = ip_info_c.fetchone()
    connection.close()
    return ip_info
 except sqlite3.OperationalError:
     messagebox.showerror("DB Error", "Cannot Connect to Database")
     sys.exit()
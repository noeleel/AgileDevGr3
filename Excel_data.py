# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:23:39 2018

@author: sarhanda
"""

import os
import sqlite3
from win32com.client import constants, Dispatch

#----------------------------------------
# get data from excel file
#----------------------------------------
XLS_FILE = os.getcwd() + "\\Ingredients.xlsx"
ROW_SPAN = (3, 80)
COL_SPAN = (1, 7)
app = Dispatch("Excel.Application")
app.Visible = True
ws = app.Workbooks.Open(XLS_FILE).Sheets(1)
exceldata = [[ws.Cells(row, col).Value 
              for col in range(COL_SPAN[0], COL_SPAN[1])] 
             for row in range(ROW_SPAN[0], ROW_SPAN[1])]

#----------------------------------------
# create SQL table and fill it with data
#----------------------------------------
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE exceltable (
   id INTEGER,
   Name TEXT,
   Quantity TEXT,
   Proteinsroteins FLOAT,
   Carbohydrates FLOAT,
   Fats FLOAT,
   Calories FLOAT
)''')
for row in exceldata:
    c.execute('INSERT INTO exceltable VALUES (?,?,?,?,?,?,?)', row)
conn.commit()

#----------------------------------------
# display SQL data
#----------------------------------------
c.execute('SELECT * FROM exceltable')
for row in c:
    print (row)
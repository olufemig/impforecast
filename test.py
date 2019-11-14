import pyodbc
import pandas as pd

server = 'tcp:demoserver01.database.windows.net' 
database = 'demosql' 
username = 'olufemig' 
password = 'Just4youdawn' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
crsr = cnxn.cursor()
for table_name in crsr.tables(tableType='TABLE'):
    print(table_name)
cursor = cnxn.cursor()
sql = "Select *"
sql = sql + " From data"
print(sql)
cursor.execute(sql)
data = pd.read_sql(sql, cnxn)
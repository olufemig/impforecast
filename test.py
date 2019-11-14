import pyodbc
import pandas as pd

dfSales = pd.read_csv('data/format1.csv',header=0, index_col=None)
dfSales.describe()
msg = "hello"
print(msg)

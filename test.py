import pyodbc
import pandas as pd

dfSales = pd.read_csv('data/clean_data.csv',header=0, index_col=None)
dfSales.head()

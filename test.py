import numpy as np
import pandas as pd
import azureml.core
import os

from azureml.core.run import Run
from azureml.core.model import Model

df = pd.read_csv('data/clean_data.csv')
dfSales = df[['CUSTOMER_ID','BRANDPACK','Sales_Vol','dia_date']]
print(dfSales.head(10))


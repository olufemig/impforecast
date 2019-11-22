import numpy as np
import pandas as pd
import azureml.core
import azureml.train.automl
import os
import logging


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from azureml.core.run import Run
from azureml.core.model import Model
from azureml.core.experiment import Experiment
from datetime import datetime
from azureml.train.automl import AutoMLConfig
from azureml.train.estimator import Estimator

time_column_name = 'dia_date'
df = pd.read_csv('data/clean_data.csv',parse_dates=[time_column_name])
dfSales = df[['CUSTOMER_ID','BRANDPACK_ID','Sales_Vol','dia_date']]
dfSales.Sales_Vol = pd.to_numeric(dfSales.Sales_Vol, errors='coerce').fillna(0, downcast='infer')

print(dfSales.dtypes)


shape2 = dfSales.set_index(['dia_date', 'BRANDPACK_ID', 'CUSTOMER_ID']).\
  unstack([1, 2]).\
  resample('D').asfreq().\
  fillna(0).\
  stack([1, 2]).\
  reset_index()
  
ZeroSales = dfSales[dfSales.Sales_Vol == 0.00]

#use this to determine all stores with product sales
NonZeroSales = dfSales[dfSales.Sales_Vol != 0.00]
df1 = NonZeroSales[['CUSTOMER_ID','BRANDPACK_ID']]
NonZeroDuplicates = df1.drop_duplicates()

  
print('%d unique dates in original df' % dfSales['dia_date'].nunique())
print('%d rows in original df' % len(dfSales))
print('%d unique sales volumes in original df' % dfSales['Sales_Vol'].nunique())
print('%d unique sales volume after filling missing values' % shape2['Sales_Vol'].nunique())
print('%d unique dates after filling missing values' % shape2['dia_date'].nunique())
print('%d rows in dataframe after filling missing values' % len(shape2))
print('%d rows in dataframe with zero sales ' % len(ZeroSales))
print('%d rows in dataframe with non-zero sales ' % len(NonZeroSales))
print(NonZeroDuplicates.head(30))
#print(dfSales.groupby('Sales_Vol').count())




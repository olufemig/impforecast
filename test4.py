import numpy as np
import pandas as pd
import azureml.core
import azureml.train.automl
import os
import logging
import datetime as dt


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from azureml.core.run import Run
from azureml.core.model import Model
from azureml.core.experiment import Experiment
from datetime import datetime
from azureml.train.automl import AutoMLConfig
from azureml.train.estimator import Estimator
from datetime import datetime

time_column_name = 'dia_date'
df = pd.read_csv('data/clean_data.csv',parse_dates=[time_column_name])
dfSales = df[['CUSTOMER_ID','BRANDPACK_ID','Sales_Vol','dia_date']]
dfSales.Sales_Vol = pd.to_numeric(dfSales.Sales_Vol, errors='coerce').fillna(0, downcast='infer')
# print(dfSales.head(10))
# print(df.head(10))
# print(df.dtypes)
# print(dfSales.dtypes)
# StoreCount = dfSales['CUSTOMER_ID'].nunique()
# print(StoreCount)
# ProductCount = dfSales['BRANDPACK_ID'].nunique()
# print(ProductCount)

shape2 = dfSales.set_index(['dia_date', 'BRANDPACK_ID', 'CUSTOMER_ID']).\
  unstack([1, 2]).\
  resample('D').asfreq().\
  fillna(0).\
  stack([1, 2]).\
  reset_index()

shape2['sales_year'] = pd.DatetimeIndex(shape2['dia_date']).year  
print(shape2['sales_year'].value_counts())
print('%d unique dates in original df' % dfSales['dia_date'].nunique())
print('%d rows in original df' % len(dfSales))
print('%d unique sales volumes in original df' % dfSales['Sales_Vol'].nunique())
print('%d unique sales volume after filling missing values' % shape2['Sales_Vol'].nunique())
print('%d unique dates after filling missing values' % shape2['dia_date'].nunique())
print('%d rows in after filling missing values' % len(shape2))

print(shape2.head(10))

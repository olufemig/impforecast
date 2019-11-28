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
# read date and include weekday flag
time_column_name = 'dia_date'
df2 = pd.read_csv('data/clean_data.csv',parse_dates=[time_column_name])
#df['CUSTOMER_ID'] = str(df['CUSTOMER_ID'])
df = df2[['CUSTOMER_ID','BRANDPACK_ID','Sales_Vol','dia_date']]
df['sales_year'] = pd.DatetimeIndex(df['dia_date']).year
print(df.dtypes)
df2010 = df[(df.sales_year == 2010) & (df.CUSTOMER_ID == 1000041)]
#df2010 = df.query('sales_year == 2010')
print(df2010.dtypes)
# #print(df2010.describe())
print(df2010.head(10))
print(df2010['sales_year'].value_counts())
print(df2010['CUSTOMER_ID'].value_counts())
# print(df2010.dtypes)

# # add missing dates
# # dfFilled2016 = dfSales.set_index(['dia_date', 'BRANDPACK_ID', 'CUSTOMER_ID']).\
# #   unstack([1, 2]).\
# #   resample('D').asfreq().\
# #   fillna(0).\
# #   stack([1, 2]).\
# #   reset_index()

# df2016['sales_year'] = pd.DatetimeIndex(df2016['dia_date']).year
# df2016only = df2016.query('sales_year == 2016')
# print(df2016only.describe())
# print(df2016only.head(10))
# print(df2016only['sales_year'].value_counts())
#  #convert customer_id to string
# # dfFilled2016['CUSTOMER_ID'] = str(dfFilled2016['CUSTOMER_ID'])
# # print(dfFilled2016.dtypes)
# # print('%d total rows in initial dataframe  ' % len(df))
# # print('%d rows in 2016 dataframe  ' % len(df2016))
# # print('%d rows in filled 2016 dataframe  ' % len(dfFilled2016))
# # #print(dfSales['sales_year'].value_counts())
# # print(dfSales['CUSTOMER_ID'].value_counts())
# # print(dfFilled2016.dtypes)
# # #print(dfFilled2016.head(30))
# # #dfZeros = dfFilled2016.query('Sales_Vol > 0')
# # #print(dfZeros.head(20))
# # # print(dfSales.query('sales_year == 2010').count())
# # # print(dfSales.query('sales_year == 2011').count())
# # # print(dfSales.query('sales_year == 2012').count())
# # # print(dfSales.query('sales_year == 2013').count())
# # # print(dfSales.query('sales_year == 2014').count())
# # # # use this to determine all stores with no product sales
# # # AllZeroSales = dfSales[dfSales.Sales_Vol == 0.00]
# # # df1 = AllZeroSales[['CUSTOMER_ID','BRANDPACK_ID']]
# # # StoresWithNoProdSales = df1.drop_duplicates()
# # # StoresWithNoProdSales['CUSTOMER_ID'] = str(StoresWithNoProdSales['CUSTOMER_ID'])

# # # #print(AllZeroSales.head(10))

# # # #Store/Product comnbos with sales
# # # l=['CUSTOMER_ID','BRANDPACK_ID']
# # # StoresWithProductsData=shape2.merge(StoresWithNoProdSales[l],on=l,indicator=True,how='outer').loc[lambda x : x['_merge']=='left_only'].copy() 
# # data2016_csv = dfFilled2016.to_csv ('data/2016_data.csv', index = None, header=True) 
# # #data2009_csv = dfFilled2009.to_csv ('data/2009_data.csv', index = None, header=True) 
# # #swp_csv = StoresWithProductsData.to_csv ('data/swp.csv', index = None, header=True) 
  
# # # print('%d unique dates in original df' % dfSales['dia_date'].nunique())
# # # print('%d rows in original df' % len(dfSales))
# # # print('%d unique sales volumes in original df' % dfSales['Sales_Vol'].nunique())
# # # print('%d unique sales volume after filling missing values' % shape2['Sales_Vol'].nunique())
# # # print('%d unique dates after filling missing values' % shape2['dia_date'].nunique())
# # # print('%d rows in dataframe after filling missing values' % len(shape2))
# # # #print('%d rows in dataframe with zero sales ' % len(ZeroSales))
# # # #print('%d rows in dataframe with non-zero sales ' % len(NonZeroSales))
# # # print(shape2.head(10))
# # # #print(dfSales.groupby('Sales_Vol').count())

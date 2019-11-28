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

# read date and include weekday flag
time_column_name = 'dia_date'
#df = pd.read_csv('data/clean_data.csv',parse_dates=[time_column_name])
df = pd.read_csv('data/clean_data.csv')
df['year'] = df['dia_date'].dt.year
#df['weekday']=np.where(((df['dia_date']).dt.dayofweek) < 5,0,1)
#df['CUSTOMER_ID'] = str(df['CUSTOMER_ID'])
# df['sales_date'] = datetime.strptime(df['dia_date'], "%Y-%m-%d")
# df['sales_year'] = df['sales_year'].year
print(df.dtypes)
# df.Sales_Vol = pd.to_numeric(df.Sales_Vol, errors='coerce').fillna(0, downcast='infer')
# dfSales = df[['dia_date','weekday','CUSTOMER_ID','BRANDPACK_ID','Sales_Vol']]

# print(dfSales.dtypes)

# # add missing dates
# shape2 = dfSales.set_index(['dia_date', 'BRANDPACK_ID', 'CUSTOMER_ID']).\
#   unstack([1, 2]).\
#   resample('D').asfreq().\
#   fillna(0).\
#   stack([1, 2]).\
#   reset_index()
  
#  #convert customer_id to string
# shape2['CUSTOMER_ID'] = str(shape2['CUSTOMER_ID'])
# print(shape2.dtypes)

# # use this to determine all stores with no product sales
# # AllZeroSales = dfSales[dfSales.Sales_Vol == 0.00]
# # df1 = AllZeroSales[['CUSTOMER_ID','BRANDPACK_ID']]
# # StoresWithNoProdSales = df1.drop_duplicates()
# # StoresWithNoProdSales['CUSTOMER_ID'] = str(StoresWithNoProdSales['CUSTOMER_ID'])

# #print(AllZeroSales.head(10))
# shape2['sales_year'] = pd.DatetimeIndex(shape2['dia_date']).year
# swp = shape2.query('sales_year == 2016')
# #Store/Product comnbos with sales
# l=['CUSTOMER_ID','BRANDPACK_ID']
# StoresWithProductsData=shape2.merge(StoresWithNoProdSales[l],on=l,indicator=True,how='outer').loc[lambda x : x['_merge']=='left_only'].copy() 
# #swp_csv = StoresWithProductsData.to_csv ('data/stores_with_product.csv', index = None, header=True) 
# fulldata_csv = swp.to_csv ('data/full_dataset1.csv', index = None, header=True) 
# #swp_csv = StoresWithProductsData.to_csv ('data/swp.csv', index = None, header=True) 
# print(swp['sales_year'].value_counts())  
# print('%d unique dates in original df' % dfSales['dia_date'].nunique())
# print('%d rows in original df' % len(dfSales))
# print('%d unique sales volumes in original df' % dfSales['Sales_Vol'].nunique())
# print('%d unique sales volume after filling missing values' % shape2['Sales_Vol'].nunique())
# print('%d unique dates after filling missing values' % shape2['dia_date'].nunique())
# print('%d rows in dataframe after filling missing values' % len(shape2))
# #print('%d rows in dataframe with zero sales ' % len(ZeroSales))
# #print('%d rows in dataframe with non-zero sales ' % len(NonZeroSales))
# print(shape2.head(10))
# #print(dfSales.groupby('Sales_Vol').count())




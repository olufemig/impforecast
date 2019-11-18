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
print(dfSales.head(10))
print(df.head(10))
print(df.dtypes)
print(dfSales.dtypes)

# Fill in blank dates and data
# dfSales.index=pd.to_datetime(df.dia_date).date
# dfSales=dfSales.groupby([dfSales.index,df['CUSTOMER_ID'],df['BRANDPACK_ID']]).agg({'Sales_Vol':'sum'}).reset_index(level=[1,2])
# drange=pd.date_range(end=df.index.max(),periods =5)
# idx=pd.MultiIndex.from_product([drange,df.cust_id.unique(),df.txn_type.unique()])
# Newdf=df.set_index(['cust_id','txn_type'],append=True).reindex(idx,fill_value=0).reset_index(level=[1,2])
# Newdf
# Setup AutoML parameters
#

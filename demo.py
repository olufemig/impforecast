import pandas as pd
import numpy as np

products = ['tablet', 'laptop', 'phone']
stores = ['downtown', 'subburb', 'supermall']

date_range = pd.date_range('2019-01-01', '2019-03-31')

# create a sample data frame
df = pd.DataFrame({
  'date': date_range,
  'product': np.random.choice(products, len(date_range)),
  'store': np.random.choice(stores, len(date_range)),
  'sales_amt': np.random.normal(50, 10, len(date_range))
})
# remove some dates
df = df[~df.date.isin(['2019-01-10', '2019-01-11', '2019-02-07'])]

# set date as index, pivot product & store, fill na with 0
# reindex & unpivot

shape2 = df.set_index(['date', 'product', 'store']).\
  unstack([1, 2]).\
  resample('D').asfreq().\
  fillna(0).\
  stack([1, 2]).\
  reset_index()

print('%d unique dates in original df' % df['date'].nunique())
print('%d rows in original df' % len(df))
print('%d unique dates after filling missing values' % shape2['date'].nunique())
print('%d rows in after filling missing values' % len(shape2))
print(shape2.head(50))
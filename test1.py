import pandas as pd
import numpy as np


time_column_name = 'dia_date'
df1 = pd.read_csv('data/clean_data.csv',parse_dates=[time_column_name])
dfSales = df1[['CUSTOMER_ID','BRANDPACK_ID','Sales_Vol','dia_date']]
# dfSales["dia_date"] = pd.to_datetime(dfSales["dia_date"])
dfSales.columns = ['store', 'product','sales', 'date']
print(dfSales.head(5))

rows = []
for date in pd.date_range(dfSales["date"].min(), dfSales["date"].max()):
    for product in np.sort(dfSales["product"].unique()):
        for store in np.sort(dfSales["store"].unique()):
            rows.append({"date": date, "product": product, "store": store})
df0 = pd.DataFrame(rows)


df_full = df0.merge(dfSales, on=["date", "product", "store"], how="left")
df_full = df_full.fillna(0)

print('%d unique dates in original df' % dfSales['date'].nunique())
print('%d rows in original df' % len(dfSales))
print('%d unique sales volumes in original df' % dfSales['sales'].nunique())
print('%d unique sales volume after filling missing values' % df_full['sales'].nunique())
print('%d unique dates after filling missing dates and values' % df_full['date'].nunique())
print('%d rows in after filling missing values' % len(df_full))
print(df_full.head(10))

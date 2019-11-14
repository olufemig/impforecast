import numpy as np
import pandas as pd
import azureml.core
import os

dfSales = pd.read_csv('data/clean_data.csv')
print(dfSales.head(5))


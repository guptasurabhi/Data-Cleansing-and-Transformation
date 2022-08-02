import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

import statistics

data = pd.read_csv('Train.csv')
test_data = pd.read_csv('Test.csv')

#########################################################################
# reduce data quantity to process with a few
# this is not used continuously, only to quickly debug code
sdata = data.iloc[0:5000, :]
sdata.to_csv('sdata.csv')
print(sdata)
#########################################################################

# print columns
print(data.columns)

# print head set
print(data.head())

# get shape of the data to visualise observations
print(data.shape)
# Dataset consists of 13647309 observations and 48 characteristics

# get description of data
print(data.describe)

# Examine NaN values across dataframe
# entire dataframe
nan_dataframe = data.isna().sum().sum()
print(f'Total Dataframe nan: {nan_dataframe}')


#######  Data Cleansing and Transformation

# strategy to replace nan values
# the strategy to replace the NaN values is explored with 0 and using mean values

filled_nan_dataframe = data.isna().sum().sum()
print(f'\nTotal NaN before fillna 0: {filled_nan_dataframe}')
data = data.fillna(0)

filled_nan_dataframe = data.isna().sum().sum()
print(f'Total NaN after fillna 0: {filled_nan_dataframe}')

print(f'Data for active cusotmers: {data.ind_nuevo.values}')
data_fill_nan = data.ind_nuevo.isna().sum().sum()
print(f'Total Dataframe nan after fillna mean: {data_fill_nan}')

# under customer  column
data_fill_nan = data.ind_nuevo.isna().sum().sum()
print(f'Customer active nan: {data_fill_nan}')

# Plot the percentiles using matplotlib
group = data.groupby('ind_nuevo')

#### Exploratory data analysis with seaborn
# Scatterplot analysis - age againts customer first contract holder
age_data = data.fillna(0)
sns.barplot(x=age_data. ind_cco_fin_ult1, y=age_data.ind_nuevo)
# sns.lmplot(x='age', y='ind_nuevo', data=age_data, fit_reg=False, hue='Stage')
plt.show()

sns.barplot(x=age_data. ind_cco_fin_ult1, y=age_data.ind_nuevo)
# sns.lmplot(x='age', y='ind_nuevo', data=age_data, fit_reg=False, hue='Stage')
plt.show()
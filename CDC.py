"""
COVID-19_Case_Surveillance_Public_Use_Data.csv
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x=pd.read_csv("C:/Users/micha/Downloads/COVID-19_Case_Surveillance_Public_Use_Data.csv")
x.to_csv('write_new_file.csv')
x["cdc_report_dt"].count
x.columns
x.head(5)
x['age_group']
x[['age_group','cdc_report_dt','sex']]
x.age_group
y=x[x.death_yn.eq("Yes")].groupby(['cdc_report_dt']).size()
x.groupby(['death_yn']).size()  # .sum() .count()  .mean()
x.iloc[4,3]  # find row 4 column 3
x.loc[x.sex=='male']  # filter on condition
x.describe()  # like summary(x) in R
x["y"]=3  # add a column called y
x = x.drop(columns=['y'])  # remove that new column
for index,row in x.iterrows():

sns.lineplot(x=y.index, y=y.values)
plt.show()

x=pd.read_csv("C:/Users/micha/Downloads/invest.csv")
x=x[['month','balance']]
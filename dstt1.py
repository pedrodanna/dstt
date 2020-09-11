#Pandas
import pandas as pd

#Data frame to be cleaned
df = pd.read_csv(r'data\US_births_1994-2003_CDC_NCHS.csv')

#Droping useless columns
df.drop(['year', 'date_of_month', 'day_of_week'], axis=1, inplace=True)

#Grouping by element
df = df.groupby(by='month').sum()

#Plotting data
df.plot()
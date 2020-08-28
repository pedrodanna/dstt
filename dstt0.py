import pandas as pd

url = "https://en.wikipedia.org/wiki/Economy_of_the_United_States"

df = pd.read_html(url)[1]
df = df.iloc[:21,:2]
df.set_index('Year', inplace=True)
df.columns = ['GDP']

df.plot(color='blue', ylabel='US Billion Dollars', title='US GDP 2000-2020',
        kind='bar', yticks=range(0, 22001, 2000)).invert_xaxis()
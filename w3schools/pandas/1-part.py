import pandas as pd

df = pd.read_csv('data.csv') # it's just an example, I don't have this file

df.dropna(inplace = True) # changes the original DataFrame
a = df.dropna() # returns a new DataFrame with rows with null values removed
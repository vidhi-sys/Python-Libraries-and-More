import pandas as pd 
poke= pd.read_csv('pokemon_data.csv')
print(poke.columns)
print(poke['Name'])#read each columns
print(poke.iloc[1:4])# reading rows 1 to 4
print(poke.iloc[2,1])# reading specific location 

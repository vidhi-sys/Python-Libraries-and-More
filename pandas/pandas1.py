import pandas as pd
#loading data into pandas
poke = pd.read_csv("pokemon_data.csv")
print(poke)
print(poke.head(2))#top 3 rows easier to read data
#without delimiter it wouldnt dispaly in form of rows or columns 
#df_xlsx=pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx)
df=pd.read_csv('pokemon_data.txt',delimiter='\t')
print(df)

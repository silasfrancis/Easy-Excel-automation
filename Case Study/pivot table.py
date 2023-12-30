import pandas as pd

df = pd.read_excel('supermarket_sales.xlsx')

df = df[['Gender', 'Product line', 'Total']] # use [] for selecting just 1 column and [[]] for multiple
#print(df)

pivot_table = df.pivot_table(index= 'Gender', columns='Product line',
                             values='Total', aggfunc='sum')#.round(0) # aggfunc is the operation you want to apply
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)
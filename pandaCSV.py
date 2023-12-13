import pandas as pd
data={'Name':['Alice','Bob','Charlie'],'Age':[25,30,35],'City': ['New York', 'San Francisco', 'LosAngeles']}
df = pd.DataFrame(data)
print("The dataframe is:")
print(df)
de = pd.read_csv('sales_data.csv')
print(de.head())
num_rows, num_columns = de.shape
print("The number of rows are:", num_rows)
print("The number of columns:", num_columns)
revenue_sum = de['Revenue'].sum()
print("The sum of the revenue:", revenue_sum)
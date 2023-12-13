import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
num_cities = 100
data = pd.DataFrame({
'City': [f'City {i}' for i in range(1, num_cities + 1)],
'Population': np.random.randint(100000, 1000000, num_cities),
'Income': np.random.normal(50000, 15000, num_cities),
'Education': np.random.normal(16, 3, num_cities)})
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Income', y='Education', size='Population', hue='Population', data=data,
palette='viridis', sizes=(20, 400), alpha=0.7)
plt.title('Bubble Chart - Income vs. Education by City')
plt.xlabel('Income')
plt.ylabel('Education')
plt.legend(title='Population')
plt.show()
plt.figure(figsize=(10, 5))
sns.kdeplot(x='Income', y='Education', data=data, cmap='viridis', fill=True)
plt.title('Density Chart - Income vs. Education by City')
plt.xlabel('Income')
plt.ylabel('Education')
plt.show()
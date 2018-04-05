import pandas as pd
import numpy as np
from scipy.stats import variation 

df = pd.read_excel('rent_dataset.xlsx')

print("Mean of the Dataset",df.mean())
print("Median of the Dataset",df.median())
print("Mode of the Dataset",df.mode())

Freq_df = pd.DataFrame(df['Rent'].value_counts()).reset_index()

Freq_df.rename(index=str, columns = {"index":"Rent","Rent":"Frequency"},inplace=True)
Freq_df['Cumulative_frequency'] = Freq_df.Frequency.cumsum()
print("Cumulative Frequency table\n\n",Freq_df)
print("Coefficient of Variance",str(variation(df['Rent'])*100)+"\n")

print("Calculate 25 percentile",np.percentile(df['Rent'], 25))
print("Calculate 50 percentile",np.percentile(df['Rent'], 50))
print("Calculate 75 percentile",np.percentile(df['Rent'], 75))
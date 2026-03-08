import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]})

# Identify missing values
print(df.isnull().sum())

# Technique 1: Drop rows with any NaN
df_dropped = df.dropna()

# Technique 2: Fill NaN with mean (Imputation)
df_filled = df.fillna(df.mean())

print("Original:\n", df)
print("Filled:\n", df_filled)

import pandas as pd

# .loc is label-based selection
# .iloc is integer-based (position) selection
df = pd.DataFrame({
    'Metric': ['Accuracy', 'Loss', 'Latency'],
    'Value': [0.98, 0.02, 15]
}, index=['m1', 'm2', 'm3'])

# Selecting specific rows/columns
print(df.loc['m1', 'Value'])      # Get 0.98 by label
print(df.iloc[0, 1])               # Get 0.98 by position

# Boolean Indexing: Selecting models with Value > 0.5
print(df[df['Value'] > 0.5])

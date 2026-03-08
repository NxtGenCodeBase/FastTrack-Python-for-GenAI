import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

# Check versions to ensure environment is set correctly
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")

# Quick Visual Sample with Seaborn
tips = sns.load_dataset("tips")
print("First 5 rows of sample 'tips' data:")
print(tips.head())
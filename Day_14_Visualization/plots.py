import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load sample dataset
tips = sns.load_dataset("tips")

# Create a figure with two subplots
plt.figure(figsize=(10, 5))

# 1. Bar plot using Seaborn
plt.subplot(1, 2, 1)
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Bill by Day")

# 2. Scatter plot using Matplotlib
plt.subplot(1, 2, 2)
plt.scatter(tips['total_bill'], tips['tip'], alpha=0.5)
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.tight_layout()
plt.show()

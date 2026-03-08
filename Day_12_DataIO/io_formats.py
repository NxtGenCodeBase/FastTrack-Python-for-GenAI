import pandas as pd

# Reading from different sources
# Replace with your local paths or public URLs
csv_df = pd.read_csv('data.csv')
json_df = pd.read_json('config.json')

# Exporting to Excel (requires 'openpyxl' library)
csv_df.to_excel('output_report.xlsx', index=False)

# Pro Tip: Use .head() to preview large datasets
print(csv_df.head(5))

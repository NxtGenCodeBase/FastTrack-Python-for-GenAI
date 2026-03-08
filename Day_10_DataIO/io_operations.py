import pandas as pd

data = {
    "Model": ["BERT", "ResNet", "YOLO"],
    "Type": ["NLP", "Vision", "Vision"],
    "Accuracy": [0.92, 0.88, 0.95]
}

df = pd.DataFrame(data)

# Saving data to CSV
df.to_csv("ai_models_data.csv", index=False)

# Reading from a URL or Local File
# url = "https://raw.githubusercontent.com"
# iris_df = pd.read_csv(url)

print("Data successfully exported to CSV.")

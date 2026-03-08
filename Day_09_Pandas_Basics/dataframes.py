import pandas as pd

# Creating a DataFrame from scratch
data = {
    "Model": ["BERT", "ResNet", "YOLO"],
    "Type": ["NLP", "Vision", "Vision"],
    "Accuracy": [0.92, 0.88, 0.95]
}

df = pd.DataFrame(data)

# Basic Indexing & Selection
print(df[df["Accuracy"] > 0.90])  # Filter models with >90% accuracy

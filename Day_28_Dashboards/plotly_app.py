import plotly.express as px
import pandas as pd

df = pd.DataFrame({"Prompt": ["A", "B", "C"], "Score": [0.9, 0.7, 0.85]})
fig = px.bar(df, x="Prompt", y="Score", title="AI Model Performance")
fig.show()

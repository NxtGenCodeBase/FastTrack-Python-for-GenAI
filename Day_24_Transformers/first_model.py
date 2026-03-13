from transformers import pipeline

# The simplest way to use AI: Sentiment Analysis
classifier = pipeline("sentiment-analysis")
result = classifier("I love learning Python for AI!")
print(result)  # Output: POSITIVE

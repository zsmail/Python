from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Load the pre-trained model and tokenizer
model = BertForSequenceClassification.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis", num_labels=3)
tokenizer = BertTokenizer.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis")

# Create a pipeline for sentiment analysis
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# User input
user_input = input("Enter a sentence for sentiment analysis: ")

# Analyzing the input sentence
results = nlp([user_input])

# Formatting the output
for result in results:
    print(f"Sentence: \"{user_input}\"")
    print(f"Sentiment: \"{result['label']}\" with {result['score'] * 100:.2f}% confidence\n")

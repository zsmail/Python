from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# User input for the article
user_article = input("Enter the text you want to summarize:\n")

# Summarizing the user input article
summary = summarizer(user_article, max_length=128, min_length=30, do_sample=False)

# Printing the summary
print("\nSummary:")
for item in summary:
    print(item['summary_text'])

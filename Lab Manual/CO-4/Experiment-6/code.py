from textblob import TextBlob

# Get sentence
text = input("Enter a sentence: ")

# Find sentiment
blob = TextBlob(text)
score = blob.sentiment.polarity

print("Sentiment Score:", score)

if score > 0:
    print("Positive Sentiment")
elif score < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")

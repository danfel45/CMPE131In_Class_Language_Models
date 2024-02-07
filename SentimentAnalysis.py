from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    text = input("Enter the text string: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment of the text string is:", sentiment)

if __name__ == "__main__":
    main()

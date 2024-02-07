from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    text = input("Enter the text you want to analyze: ")
    sentiment = analyze_sentiment(text)
    print("Sentiment of the text is:", sentiment)

if __name__ == "__main__":
    main()

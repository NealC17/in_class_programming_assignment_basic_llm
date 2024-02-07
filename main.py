from textblob import TextBlob

def analyze_sentiment(input_string):
    # Create a TextBlob object
    blob = TextBlob(input_string)

    # Get the sentiment polarity
    polarity = blob.sentiment.polarity

    # Determine the sentiment
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    else:
        return "Negative"


if __name__ == "__main__":
    # Ask the user to input a string
    user_input = input("Enter a string: ")

    # Analyze the sentiment of the input
    sentiment = analyze_sentiment(user_input)

    # Print the sentiment result
    print(f"The sentiment of the input string is: {sentiment}")
    
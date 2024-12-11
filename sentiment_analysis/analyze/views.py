from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from textblob import TextBlob
from transformers import pipeline

'''
def sentiment_analysis(request):
    result = None
    sentiment = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment = "😊 Positive Sentiment"
        elif polarity < 0:
            sentiment = "😠 Negative Sentiment"
        else:
            sentiment = "😐 Neutral Sentiment"

        result = {'input': user_input, 'sentiment': sentiment}

    return render(request, 'analyze/sentiment.html', {'result': result})

    '''

from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(sentence):
    result = sentiment_pipeline(sentence)
    label = result[0]['label']
    score = result[0]['score']
    return f"Sentiment: {label} (Confidence: {score:.2f})"

# User input
sentence = input("Enter a sentence for sentiment analysis: ")
print(analyze_sentiment(sentence))


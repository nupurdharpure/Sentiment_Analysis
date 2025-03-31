from django.shortcuts import render
from textblob import TextBlob

def analyze_sentiment(request):
    sentiment_result = None
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            analysis = TextBlob(text)
            sentiment_score = analysis.sentiment.polarity
            if sentiment_score > 0:
                sentiment_result = "Positive"
            elif sentiment_score < 0:
                sentiment_result = "Negative"
            else:
                sentiment_result = "Neutral"
    
    return render(request, 'sentiment/index.html', {'sentiment_result': sentiment_result})

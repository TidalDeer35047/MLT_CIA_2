from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_vader(sentence):

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)
    negative = sentiment_dict['neg']
    neutral = sentiment_dict['neu']
    positive = sentiment_dict['pos']
    compound = sentiment_dict['compound']

    if sentiment_dict['compound'] >= 0.05 :
        overall_sentiment = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
        overall_sentiment = "Negative"

    else :
        overall_sentiment = "Neutral"
  
    return(negative, neutral, positive, compound, overall_sentiment)

    #"The sentiment scores of the  prompt are as follows:\nNegative: ",negative, "\nNeutral: ", neutral, "\nPositive: ", positive, "\nCompound: ", compound, "\nThe overall sentiment is: ", overall_sentiment
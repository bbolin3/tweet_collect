import tweepy

consumer_key = 'cykRTcVpJZfs5QQTFwLxqn7pD'
consumer_secret = 'x6XwVSQujvbEGRCDn22wwY1fDs5Nlu6PDven5DfUJHY5GG9ziQ'
access_token = '758889338289524736-GND0t04FIK66pF97vTiFtRmweimyFTl'
access_token_secret= 'p5gT2ozy6hnjGGvaXlc8yAWgS8V7Bp8DMstqVkGqPQQkV'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
tweets = []
for tweet in public_tweets:
    tweets.append(tweet.text)
    print('\n'*5,tweet.text)




from nltk.tokenize import sent_tokenize, word_tokenize

print(word_tokenize(tweets[0]))



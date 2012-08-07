import tweepy

# Get tokens
from tokens import *

# Let's say this is a web app, so we need to re-build the auth handler
# first...
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def getFollowerTweets(vapi, num=20):
    """
    Gets the specified number in chronological order from the 
    authenticated user's timeline.
    """
    statuses = vapi.friends_timeline(count=num)
    parsed = []
    for s in statuses:
        parsed.append(unicode(s.text))
    return parsed

class Words:
    
    def __init__(self, tweets, ignored=[]):
        self.__tweets  = tweets
        self.__ignored = ignored
        self.__words = self.parseWords(self.__tweets)
        self.printWords()
    
    def parseWords(self, tweets):
        parsed = []
        for tweet in tweets:
            words = tweet.split()
            for w in words:
                if not (w in self.__ignored): parsed.append(w)
        return parsed
    
    def printWords(self):
        for w in self.__words:
            print w
    
            

def analyseTweets(tweets):
    """
    Analyses a list of tweets (plain text)
    """
    words = Words(tweets)
            

p = getFollowerTweets(api, 5)
for i in range(0, len(p)):
    print i, p[i]
analyseTweets(p)

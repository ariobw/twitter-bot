#! python3
# twitter_bot.py - Prototype for my first twitter bot using tweepy

import tweepy
from secrets import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def tweet_text():
    """Create the text of the tweet you want to send."""
    text = ''
    return text


def tweet(text):
    """Send out the text as a tweet."""
    try:
        api.update_status(text)
    except tweepy.error.TweepError as err:
        print(err)


def get_public_timeline():
    """Print public tweets/home timeline"""
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


def get_user_friend():
    # Get the user object for twitter
    username = input('Insert Twitter username: ')
    user = api.get_user(username)

    print(user.screen_name)
    print(user.followers_count)
    for friend in user.friend():
        print(friend.screen_name)


# Stream tweet
# Creating a StreamListener
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False


# Creating a stream
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Starting a stream (example)
# myStream.filter(track=['python'])  # stream all tweets containing the word python

myStream.filter(follow=['3243302592'])  # stream tweets by a specific user

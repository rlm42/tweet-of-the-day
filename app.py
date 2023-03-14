import tweepy
import time as _time
from flask import Flask, request, render_template

app = Flask(__name__)


# Bot logging in to Twitter.
consumer_key = "Wjyy4qzaFbvtJBweeViuydH6o"
consumer_secret = "J61Z3ZiUplDjRhNQSGFykUNaiuXxqvJvE6RjKfe0zqtARBXtuV"
access_token = "82548025-C99p7amZmFGmzsZbZddTvqSPgFU4xBEXASN4PeGZy"
access_secret = "AQaHCPAEk73T4gikqGJnpVfHPihNlh5g2WVruQkp0wxyI"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
# tweets = api.search_tweets(q='#crypto', count=10, result_type='popular', tweet_mode='extended')

# columns = ['User', 'Tweet']
# data = []

# for tweet in tweets:
#     data.append([tweet.user.screen_name, tweet.full_text])

@app.route("/")
def main():
    while True:
        tweets = api.search_tweets(q='#crypto', count=10, result_type='popular', tweet_mode='extended')
        columns = ['User', 'Tweet', 'Likes', 'Favourites']
        data = []
        for tweet in tweets:
            data.append([tweet.user.screen_name, tweet.full_text, tweet.retweet_count, tweet.favorite_count])
        # _time.sleep(86400)  # in seconds (this is 24 hours)
        return(data)
        _time.sleep(86400)  # in seconds (this is 24 hours)
        # return foo()


if __name__ == "__main__":
    # run()
    app.run(debug=True)


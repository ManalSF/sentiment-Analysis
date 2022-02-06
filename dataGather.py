import tweepy as tw
import tweepy
import pandas as pd

CONSUMER_KEY = "Fe8kUqfANx6xJcezgkKAuSBoG"
CONSUMER_SECRET_KEY = "BUAvtmmNMYyzmoUumGueNsLvy7jfMUEP878n7RMVo9BidRc4LP"
ACCESS_KEY = "1433162692378959875-HeoRJcklsOzJ7GQWKMRfyCih4qJWQ1"
ACCESS_KEY_SECRET = "PLTQadBFLJU65Nqw2OSpNrZEyiAsxQot2o7PFz9u9PJWj"

auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)
api = tw.API(auth)

tweet_list = []
list = []


class Collector():

    def __init__(self, kword, noTweets):
        self.keyword = kword
        self.noOfTweet = noTweets

    def tweetList(self):
        return list

    def main(self):
        keyword = self.keyword + " -filter:retweets"
        # print(self.keyword)
        tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(self.noOfTweet)
        # print(self.noOfTweet)
        list = tweets

        for tweet in tweets:
            # print(tweet.text)
            tweet_list.append(tweet.text)

        tw_list = pd.DataFrame(tweet_list)
        # print(tw_list)
        tw_list.to_csv('Gather.csv')

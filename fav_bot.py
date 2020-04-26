from TwitterAPI import TwitterAPI
from os import environ

# from private import *

API_KEY = environ['API_KEY']
API_KEY_SECRET = environ['API_KEY_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']
STALKED_ACCOUNT = environ['STALKED_ACCOUNT'] # '1705276416'
TWEET_TEXT = " Esto es una prueba"

class TwitterBot:
    def __init__(self, credentials):
        self.api = TwitterAPI(credentials['api_key'], 
                    credentials['api_key_secret'],
                    credentials['access_token'],
                    credentials['access_token_secret'])

    def reply_tweets(self):
        stream = self.api.request('statuses/filter', {'follow': STALKED_ACCOUNT})

        for tweet in stream:
            print(tweet['text'] if 'text' in tweet else tweet)

            if self.__is_tweet_valid(tweet):
                print(tweet['text'] if 'text' in tweet else tweet)
                self.__reply(tweet['id'])

    def fav_tweets(self):
        stream = self.api.request('statuses/filter', {'follow': STALKED_ACCOUNT})

        for tweet in stream:
            print(tweet['text'] if 'text' in tweet else tweet)

            if self.__is_tweet_valid(tweet):
                print(tweet['text'] if 'text' in tweet else tweet)
                self.__fav(tweet['id'])
                

    def __is_tweet_valid(self, tweet):
        return (('user' in tweet) &  self.__tweeted_by_stalked_account(tweet['user']['id_str']) & ('id' in tweet))

    def __tweeted_by_stalked_account(self, user_id):
        return (user_id == STALKED_ACCOUNT)

    def __reply(self, tweet_id):
        response = self.api.request('statuses/update', {'status': TWEET_TEXT, 'in_reply_to_status_id': tweet_id})
        print('SUCCESS' if response.status_code == 200 else 'PROBLEM: ' + response.text)

    def __fav(self, tweet_id):
        response = self.api.request('favorites/create', {'id': tweet_id})
        print('SUCCESS' if response.status_code == 200 else 'PROBLEM: ' + response.text)

if __name__ == "__main__":
    credentials = {
        'api_key': 'API_KEY',
        'api_key_secret':'API_KEY_SECRET',
        'access_token':'ACCESS_TOKEN',
        'access_token_secret':'ACCESS_TOKEN_SECRET'
    }

    bot = TwitterBot(credentials)
    bot.fav_tweets()
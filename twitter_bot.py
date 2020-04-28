from TwitterAPI import TwitterAPI
from text_generator import TextGenerator
import json

class TwitterBot:
    def __init__(self, credentials, stalked_account):
        self.api = TwitterAPI(credentials['api_key'], 
                    credentials['api_key_secret'],
                    credentials['access_token'],
                    credentials['access_token_secret'])

        self.text_generator = TextGenerator()
        self.stalked_account = stalked_account
        self.stalked_account_id = self.__get_stalked_account_id()

    def __get_stalked_account_id(self):
        response = self.api.request('users/show', {'screen_name':self.stalked_account})

        if response.status_code == 200:
            return  json.loads(response.text)['id_str']
        else:
            print('PROBLEM: ' + response.text)
            exit()

    def reply_tweets(self):
        stream = self.api.request('statuses/filter', {'follow': self.stalked_account_id})

        for tweet in stream:
            print(tweet['text'] if 'text' in tweet else tweet)

            if self.__is_tweet_valid(tweet):
                print(tweet['text'] if 'text' in tweet else tweet)
                self.__reply(tweet['id'])

    def fav_tweets(self):
        stream = self.api.request('statuses/filter', {'follow': self.stalked_account_id})

        for tweet in stream:
            print(tweet['text'] if 'text' in tweet else tweet)

            if self.__is_tweet_valid(tweet):
                print(tweet['text'] if 'text' in tweet else tweet)
                self.__fav(tweet['id'])
                

    def __is_tweet_valid(self, tweet):
        if 'user' in tweet:
            return (self.__tweeted_by_stalked_account(tweet) & ('id' in tweet))
        else:
            return False

    def __tweeted_by_stalked_account(self, tweet):
        return (tweet['text'][0:4] != 'RT @')

    def __reply(self, tweet_id):
        tweet_text = self.text_generator.get_random_text()
        response = self.api.request('statuses/update', {'status': f'@{self.stalked_account} {tweet_text}', 'in_reply_to_status_id': tweet_id})
        print('SUCCESS' if response.status_code == 200 else 'PROBLEM: ' + response.text)

    def __fav(self, tweet_id):
        response = self.api.request('favorites/create', {'id': tweet_id})
        print('SUCCESS' if response.status_code == 200 else 'PROBLEM: ' + response.text)


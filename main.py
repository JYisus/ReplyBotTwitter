#!/usr/bin/python3

from twitter_bot import TwitterBot
from os import environ
import utils

API_KEY = utils.getenv('API_KEY','')
API_KEY_SECRET = utils.getenv('API_KEY_SECRET','')
ACCESS_TOKEN = utils.getenv('ACCESS_TOKEN','')
ACCESS_TOKEN_SECRET = utils.getenv('ACCESS_TOKEN_SECRET','')
STALKED_ACCOUNT = utils.getenv('STALKED_ACCOUNT','')

def check_credentials(credentials):
    for item in credentials:
        if item == '':
            return False
    return True

if __name__ == "__main__":
    credentials = {
        'api_key': API_KEY,
        'api_key_secret':API_KEY_SECRET,
        'access_token':ACCESS_TOKEN,
        'access_token_secret':ACCESS_TOKEN_SECRET
    }

    if check_credentials(credentials):
        bot = TwitterBot(credentials, STALKED_ACCOUNT)
        bot.reply_tweets()
    else:
        print('Credenciales no validas')

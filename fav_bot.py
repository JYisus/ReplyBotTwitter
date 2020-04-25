from TwitterAPI import TwitterAPI
from os import environ

# from private import *

API_KEY = environ['API_KEY']
API_KEY_SECRET = environ['API_KEY_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

TRACK_TERM =  '1705276416'
TWEET_TEXT = " Esto es una prueba"
api = TwitterAPI(API_KEY, 
                    API_KEY_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET)

# TODO: Controlar que el texto del mensaje que se va a responder no es el mismo que 
# TODO: el texto que se va a responder
def reply_stream_tweets():
    r = api.request('statuses/filter', {'follow': TRACK_TERM})

    for item in r:
        print(item['text'] if 'text' in item else item)

        print(item['user'])

        print(item['user']['id'])

        if item['user']['id_str'] == TRACK_TERM :
            if 'id' in item:
                tweet_id = item['id']

            print(item['text'] if 'text' in item else item)
            t = api.request('statuses/update', {'status': TWEET_TEXT, 'in_reply_to_status_id': tweet_id})
            print('SUCCESS' if t.status_code == 200 else 'PROBLEM: ' + t.text)

def fav_tweets():
    r = api.request('statuses/filter', {'follow': TRACK_TERM})

    for item in r:
        print(item['text'] if 'text' in item else item)

        if 'user' in item:
            if item['user']['id_str'] == TRACK_TERM :
                if 'id' in item:
                    tweet_id = item['id']

                print(item['text'] if 'text' in item else item)
                t = api.request('favorites/create', {'id': tweet_id})
                print('SUCCESS' if t.status_code == 200 else 'PROBLEM: ' + t.text)

if __name__ == "__main__":
    fav_tweets()
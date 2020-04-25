from TwitterAPI import TwitterAPI

from private import *

TRACK_TERM = '759063401779920896'
TWEET_TEXT = "@YisusIsBack Esto es una prueba"
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

reply_stream_tweets()
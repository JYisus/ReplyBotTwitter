from TwitterAPI import TwitterAPI

from private import *

TRACK_TERM = '759063401779920896'
TWEET_TEXT = "@yisusisback Que te calles!"

api = TwitterAPI(API_KEY, 
                 API_KEY_SECRET,
                 ACCESS_TOKEN,
                 ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'follow': TRACK_TERM})

for item in r:
    print(item['id'] if 'id' in item else item)

    if 'id' in item:
        tweet_id = item['id']

    print(item['text'] if 'text' in item else item)

    r = api.request('statuses/update', {'status': TWEET_TEXT, 'in_reply_to_status_id': tweet_id})
    print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)


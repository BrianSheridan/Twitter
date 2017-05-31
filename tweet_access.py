import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'ff6ezmmrm1JFYKhEwyuZvLWVb'
CONSUMER_SECRET = 'oovTfeNGJGEv0pIIW9dRVQsnjRFqkO2B3Sn5S1xQPOYk7m0yfo'
OAUTH_TOKEN = '964307796-61x5gPQ09kqC6N7KV2epxZBex2KKX9uUO5c4cWeS'
OAUTH_TOKEN_SECRET = 'Og864lSY7sykY2rcEJU9uiDqGkMdQvBR8qYUBwN4og59F'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'Dublin'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
print (json.dumps (results[0]._json, indent=4))

for status in results:
    print (status.text.encode('utf-8'))
    print (status.user.id)
    print (status.user.screen_name)
    print (status.user.profile_image_url_https)
    print (status.user.followers_count)
    print (status.place)

    

    


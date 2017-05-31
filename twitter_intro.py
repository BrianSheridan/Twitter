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

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                   for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                   for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print (common_trends)

print (json.dumps(dub_trends, indent=1))
print (json.dumps(lon_trends, indent=1))





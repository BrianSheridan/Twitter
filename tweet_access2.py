import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'ff6ezmmrm1JFYKhEwyuZvLWVb'
CONSUMER_SECRET = 'oovTfeNGJGEv0pIIW9dRVQsnjRFqkO2B3Sn5S1xQPOYk7m0yfo'
OAUTH_TOKEN = '964307796-61x5gPQ09kqC6N7KV2epxZBex2KKX9uUO5c4cWeS'
OAUTH_TOKEN_SECRET = 'Og864lSY7sykY2rcEJU9uiDqGkMdQvBR8qYUBwN4og59F'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Dublin'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                                for status in results
                                        for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
                                for status in results
                                        for hashtag in status._json['entities']['hashtags'] ] 

words = [ word 
                        for text in status_texts
                                 for word in text.split() ]


#print (json.dumps(status_texts[0:5], indent=1)) 
#print (json.dumps(screen_names[0:5], indent=1)) 
#print (json.dumps(hashtags[0:5], indent=1))
#print (json.dumps(words[0:5], indent=1))

#for entry in [screen_names, hashtags, words]:
 #   counter = Counter(entry)
  #  print (counter.most_common()[:10])
   # print


for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print (table)


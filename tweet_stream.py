from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


CONSUMER_KEY = 'ff6ezmmrm1JFYKhEwyuZvLWVb'
CONSUMER_SECRET = 'oovTfeNGJGEv0pIIW9dRVQsnjRFqkO2B3Sn5S1xQPOYk7m0yfo'
OAUTH_TOKEN = '964307796-61x5gPQ09kqC6N7KV2epxZBex2KKX9uUO5c4cWeS'
OAUTH_TOKEN_SECRET = 'Og864lSY7sykY2rcEJU9uiDqGkMdQvBR8qYUBwN4og59F'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

keyword_list=['islam', 'catholicism', 'software', 'sugar']
limit = 500

class MyStreamListener(StreamListener):

    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print ("Failed on_data: %s" % str(e))
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True



twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)

from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_auth
from pymongo import MongoClient
import json

keyword = 'corbyn'
keyword_list=[keyword]
limit = 500
MONGODB_URI = "mongodb://127.0.0.1:27017"
DBS_NAME = "twitter"
COLLECTION_NAME = keyword
connection = MongoClient(MONGODB_URI)
collection = connection[DBS_NAME][COLLECTION_NAME]
class MyStreamListener(StreamListener):
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
    def on_data(self, data):
        if self.num_tweets < limit:
            self.num_tweets += 1
            try:
                tweet = json.loads(data)
                collection.insert_one(tweet)
                return True
            except BaseException as e:
                print ("Failed on_data: %s" % str(e))
            return True
        else:
            return False
    def on_error(self, status):
        print(status)
        return True
auth = get_auth()
twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
connection.close()
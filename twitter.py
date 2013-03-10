# Author: Nils Mull (mail@flash-byte.de)
# Date: 22.01.2013
from ast import literal_eval
import oauth2 as oauth
from init import twitterConfig
import sys


class Twitter(object):
    def __init__(self):
        self.consumerKey = twitterConfig['consumerKey']
        self.consumerSecret = twitterConfig['consumerSecret']
        self.tokenKey = twitterConfig['tokenKey']
        self.tokenSecret = twitterConfig['tokenSecret']
        self.__initTwitterClient__()

    def __initTwitterClient(self):
        consumer = oauth.Consumer(self.consumerKey, self.consumerSecret)
        token = oauth.Token(self.tokenKey, self.tokenSecret)
        self.client = oauth.Client(consumer, token)

    def sendTweet(self, message):
        request = "https://api.twitter.com/1.1/statuses/update.json?status=" + message
        response = self.client.request(request, method='POST')
        if response[0]['status'] != '200':
            print "Something fucked up while sending tweet: %s" % (message)
            print literal_eval(response[1])['errors'][0]["message"]
            sys.exit(99)

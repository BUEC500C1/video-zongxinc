#access token: 1165945693627809792-v3O1zGduCeiXhgfxwQV9BlIM6fTMsL
#access token secret: 4vLxm2RC4lkP30anwghf80jZbFKSyncxYPHYSrr1n8ZPN
import tweepy
from PIL import Image, ImageDraw, ImageFont

consumer_key = 'R1Yz5Zv7eaa5rFs6dL7aIMgZj'
consumer_secret = 'U6U1pbXho1KH6UIiu2b2YuiAlh02kHMYFICGmU6pSbljUngD3E'
access_token = '1165945693627809792-v3O1zGduCeiXhgfxwQV9BlIM6fTMsL'
access_token_secret = '4vLxm2RC4lkP30anwghf80jZbFKSyncxYPHYSrr1n8ZPN'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def txt2img

public_tweets = api.user_timeline(screen_name = '@realDonaldTrump', count = 1, include_rts = False)
for tweet in public_tweets:
    print(tweet.text)

#access token: 1165945693627809792-v3O1zGduCeiXhgfxwQV9BlIM6fTMsL
#access token secret: 4vLxm2RC4lkP30anwghf80jZbFKSyncxYPHYSrr1n8ZPN
import tweepy
import cv2
import glob
import pprint
import os
from PIL import Image, ImageDraw, ImageFont

consumer_key = 'R1Yz5Zv7eaa5rFs6dL7aIMgZj'
consumer_secret = 'U6U1pbXho1KH6UIiu2b2YuiAlh02kHMYFICGmU6pSbljUngD3E'
access_token = '1165945693627809792-v3O1zGduCeiXhgfxwQV9BlIM6fTMsL'
access_token_secret = '4vLxm2RC4lkP30anwghf80jZbFKSyncxYPHYSrr1n8ZPN'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')
    #encode('ascii','xmlcharrefreplace')
    #encode('ascii', 'ignore').decode('ascii')

def txt2img(txt, user, num):
	img = Image.new('RGB', (1280, 500), color = (0, 0, 0))
	font = ImageFont.truetype('./DancingScript-Bold.ttf' ,20)
	d = ImageDraw.Draw(img)
	d.text((100, 250), txt, fill = (255, 255, 255), font = font)
	filename = 'image/' + user + str(num) + '.jpg'
	img.save(filename)

name = '@realDonaldTrump'
public_tweets = api.user_timeline(screen_name = name, count = 10)
count = 0
for tweet in public_tweets:
	count = count + 1
	print(tweet.text)
	thetweet = deEmojify(tweet.text)
	txt2img(thetweet, name, count)

img_array = []
size = 0
path = '/Users/allen/Documents/GitHub/video-zongxinc/image'
for root, dirs, files in os.walk(path):
	for file in files:
		img_array.append(file)
print(len(img_array))
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'MJPG'), 0.333, (1280, 720))

for i  in range(1, len(img_array) + 1):
	img = cv2.imread('/Users/allen/Documents/GitHub/video-zongxinc/image/' + img_array[i - 1])
	img = cv2.resize(img, (1280, 720))
	out.write(img)
for e in img_array:
	print(e)
	os.remove(f'{path}/{e}')


from operator import contains
import tweepy
from datetime import datetime
import json

# created by Jack Matthews/ @makozort
# feel free to use the code anywhere but please credit me



with open(f"./keys.json", 'r') as f:
  data = json.load(f)                   # read in a jso
  consumerkey = (data["consumerkey"])
  consumersecret = (data["consumersecret"])
  accesstoken = (data["access_token"])
  accesssecret = (data["accesssecret"])



    
client = tweepy.Client( 
    consumer_key=consumerkey,
    consumer_secret=consumersecret,
    access_token=accesstoken,               # pass variables into something the client class can use
    access_token_secret=accesssecret
)

today = datetime.today()
dlcdate = datetime(day=22, month=2, year=2022)
dlcname = " The Witch Queen"

i = str(dlcdate - today) # get the time between now release of dlc
if "day" in i:    # look, it was 5am and this solved 2 problems I had
    difference = (int(i.split(" ")[0]) + 1) # and add 1 to it because it does not count the date its trying to reach as a full day
else:
    text = ("1 day until")
    client.create_tweet(text=text) # python is weird how it does datetime imo, or maybe im just dumb. either way the workaround to some issue.. well, works.
    exit()


if difference == 0: #if the dlc is out
    text = (dlcname + " is out!")
elif difference < 0: # don't send a tweet if the dlc is already out
    print("dlc already out") 
    exit()
else:
    text = (str(difference) + " days until" + dlcname)
    
client.create_tweet(text=text) # send the tweet!



# created by Jack Matthews/ @makozort
# feel free to use the code anywhere but please credit me

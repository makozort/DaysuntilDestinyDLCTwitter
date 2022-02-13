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
dlcdate = datetime(day=23, month=2, year=2022)
dlcname = " The Witch Queen"


if today.date() == dlcdate.date():
    text = (dlcname + " is out!")
    client.create_tweet(text=text)
    exit()

i = str(dlcdate - today) # get the time between now release of dlc
if "day" in i:    # look, it was 5am and this solved 2 problems I had
    difference = (int(i.split(" ")[0])) # add 1 to the difference as datetime does not add the actual day of the dlc (we want that)
else:
    text = ("1 reset until" + dlcname)
    client.create_tweet(text=text) 
    exit()

if difference < 0: # don't send a tweet if the dlc is already out
    print("dlc already out")
    exit()
else:
    text = (str(difference) + " days until" + dlcname)

client.create_tweet(text=text) # send the tweet!



# created by Jack Matthews/ @makozort
# feel free to use the code anywhere but please credit me

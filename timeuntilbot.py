import tweepy
from datetime import datetime

mylines = []                            
with open (f".\keys.txt", 'rt') as f: # here we read in our secret keys into an array
    for myline in f:                
        mylines.append(myline)
    x = (mylines[0].split("= "))                   
    consumerkey = (x[1].rstrip("\n"))
    x = (mylines[1].split("= "))
    consumersecret = (x[1].rstrip("\n"))
    x = (mylines[2].split("= "))
    accesstoken = (x[1].rstrip("\n"))
    x = (mylines[3].split("= "))            # split and sort our keys into variables 
    accesssecret = (x[1].rstrip("\n"))
    
client = tweepy.Client( 
    consumer_key=consumerkey,
    consumer_secret=consumersecret,
    access_token=accesstoken,               # pass varibles into something the client class can use
    access_token_secret=accesssecret
)

from datetime import datetime

today = datetime.now()
dlcdate = datetime(day=23, month=2, year=2022, hour=20) 


difference = str(dlcdate - today) # get the time between now release of dlc


if (difference.split(", ")[0]) == ("-1 day"): #probably ineffecient way to check if it is the day of a dlc release, but it works
    text = ("The Witch Queen is out!")
else:
    text = (difference.split(", ")[0] + " until The Witch Queen")

client.create_tweet(text=text) # send the tweet!
 





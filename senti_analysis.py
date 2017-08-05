import tweepy
from textblob import TextBlob

#Authentication and creation of the Twitter API object.
consumer_key='UoVBHiw7KcsNtTirWoNhDkg5c'
consumer_secret='DP81LuTxm5hPVIeKCsHQhCKVJruot6iuvBDqh9STuBZhZfItoT'

access_key='38836522-uHsl4eWL91V7atLmuGUnfmuqu5smZkSQg5de5GUCF'
access_secret='9NLeksWSQLg8jgh1Uc21vBVgvMAAVNp4lvI8BORLBbqay'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

api=tweepy.API(auth)

#Searching for popular tweets for the input string from the user (returns a list).
search_string=input("Enter your search string : ")

tweetList=api.search(search_string,result_type='popular')

length_of_list=len(tweetList) #Length of the tweet list
sentiSum=0 #Initialising the total sentiment variable

#Checking each tweet in tweetList for sentiment
for tweet in tweetList:
	print(tweet.text)
	t=TextBlob(tweet.text)
	print(t.polarity)
	sentiSum+=TextBlob(tweet.text).polarity

#Average sentiment = (total sentiment of the list)/(length of list)
senti=sentiSum/length_of_list
print("Sentiment : "+str(senti))

#If average sentiment is +ve, the sentiment is positive, and vice versa. Neutral sentiment is denoted by 0.
if(senti>0):
	print("Positive")
elif(senti<0):
	print("Negative")
else:
	print("Neutral")
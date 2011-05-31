import sqlite3
from twython import Twython
from time import sleep
from simpleOSC import *

db = sqlite3.connect('fintwit.db')
initOSCClient('127.0.0.1', 1337)

globaltime=0

class Place:
	id=0
	def __init__(self,coord):
		self.id=Place.id
		Place.id+=1
		self.coord = coord
		self.counter=0
		self.exponential=0
		self.lastId=44310900387229696

	def step(self,twitter):
		if(self.counter==0):
			print "ask twitter about %i"%(self.id,)
			getNum=0
			try:
				search_results = twitter.searchTwitter(geocode="%f,%f,50km"%self.coord,since_id=str(self.lastId))["results"]
				getNum=len(search_results)
			except:
				print "network error"
			try:
				c = db.cursor()
				c.execute("insert into twit2 values(?,?,?);",(self.id, getNum, globaltime))
				db.commit()
			except:
				pass
			try:
				sendOSCMsg( '/place', [self.id,getNum] )
			except:
				pass
			if getNum!=0:
				self.lastId=search_results[0]["id"]
			print getNum
			if(getNum==0):
				self.exponential=min(self.exponential+1,10)
				self.counter=2**self.exponential
			else:
				self.exponential=max(self.exponential-1,0)
			return 1
		else:
			print "dont ask twitter about %i"%(self.id,)
			self.counter-=1
			return 0


placeLat=[63.3833,62.7000,62.4000,63.8333,61.4667,61.1333,62.6833,61.4167,60.5167,63.0500,60.2167,61.0000,60.1667,60.8667,61.9667,61.0333,60.3167,63.5667,61.1833,62.6667,62.1000,63.0167,61.7333,61.9500,62.1667,68.3500,68.6167,65.7833,67.7000,66.8000,66.5667,67.3667,65.0333,64.2833,65.9667,64.9333]
placeLong=[24.2167,22.8333,25.6833,23.1167,21.8000,21.5000,22.8167,23.5833,22.2667,21.7667,24.6667,24.4500,24.9333,26.7000,25.6667,28.1333,24.9667,27.1833,28.7667,29.6333,30.1333,27.8000,27.3000,28.9500,27.8667,23.4167,27.4167,24.5833,24.8500,24.0000,25.8333,26.6500,24.8000,27.6833,29.1833,25.3667]
places=map(lambda i: Place(i), zip(placeLat,placeLong))

twitter = Twython(twitter_token="YosdwuETznl9BXpAsOy1A",
				  twitter_secret="2ePoekF4XlJ9GlF8mgCiFYXM7VhoyvtJkQ74CjXc324",
				  oauth_token="35837306-EVApsSptGdpny7R2kPoZtQOOfAMg6dvBZ7b2t1tEA",
				  oauth_token_secret="rDnKgZmB1dSqDitVcZfJVKQdVm63UyZUhrByHUP8uIc")
				  
for place in places:
	place.step(twitter)
while True:
	globaltime+=1
	for place in places:
		if place.step(twitter)==1 :
			sleep(10)


"""



for tweet in search_results["results"]:
	print tweet"""

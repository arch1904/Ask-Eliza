import pymongo
from pymongo import MongoClient
import datetime as dt


client = MongoClient()

db = client['User-Data']
collection = db['User-Data']

def add_user(name,email,comments):
	curr_user = {"name": name,
	 "date": dt.datetime.utcnow(),
	 "email":email,
	 "comments": comments}

	post = db.posts.find({"name":name})
	inside = False
	for doc in post:
		inside = True
		if (doc["name"]!=name) and  (doc["email"]!=email):
			post_id = db.posts.insert_one(curr_user).inserted_id
			return post_id
	if not inside:
		post_id = db.posts.insert_one(curr_user).inserted_id
		return post_id
	return False

	#return post_id

def register_last_session(name,comment):
	post = db.posts.find({"name":name})
	for doc in post:
		curr_user = {"name": doc["name"],
		 "date": doc["date"],
		 "email":doc["email"],
		 "comments":comment}
		post_id = db.posts.update({'_id':doc["_id"]},curr_user,upsert=False)
		#break

	post = db.posts.find({"name":name})
	for doc in post:
		print doc

def view_db(name):
	post = db.posts.find({"name":name})
	for doc in post:
		print doc


#print add_user('Archit','archit.941@gmail.com','something')
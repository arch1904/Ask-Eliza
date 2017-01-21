import pymongo
from pymongo import MongoClient
import datetime as dt

client = MongoClient()

db=client['User-Data']
collection = db['User-Data']
posts = db.posts
def add_user(name,email,comments):
	curr_user = {"name": name,
	 "date": dt.datetime.utcnow(),
	 "email":email, 
	 "comments": comments}

	posts = db.posts
	post_id = posts.insert_one(curr_user).inserted_id







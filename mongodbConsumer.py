from pymongo import MongoClient
from json import loads
from sys import stdin

client = MongoClient('mongodb+srv://csp554:sharepassword@cluster0.ikcx0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
collection = client.CSP554.COVID

for line in stdin:
	try:
		print(line)
		collection.insert_one(loads(line))
	except:
		pass

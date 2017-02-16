import pymongo

#establish a connection
connection = pymongo.MongoClient("mongodb://localhost", 27017)

#get stories collection from reddit db
db = connection.reddit
stories = db.stories

import pymongo

#establish a connection
connection = pymongo.MongoClient("mongodb://localhost", 27017)

#use school db and get scores collection
db = connection.school
scores = db.scores


def find_project():
    project = {'student_id':1, '_id':0, 'score':1}
    query = {'score':{'$gt':90, '$lt':92}}
    doc = scores.find(query,project)
    for it in doc:
        print it


if __name__ == "__main__":
    find_project()
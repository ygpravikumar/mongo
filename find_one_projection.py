import pymongo

#create a connection to DB
connection = pymongo.MongoClient("mongodb://localhost", 27017)

#get the scores DB
db = connection.school
scores = db.scores

def find_one_project():
    project = {'student_id':1, '_id':0, 'score':1}
    query = {'student_id':10.0}
    doc = scores.find(query,project)
    for it in doc:
        print it


if __name__ == "__main__":
    find_one_project()
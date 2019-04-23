import pymongo

client = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db = client.test


def get_all() :
    return list(db.posts.find({}))
    


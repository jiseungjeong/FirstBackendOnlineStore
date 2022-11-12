import pymongo

MONGO_URI="mongodb+srv://jiseungjeong:jiseungjeong@cluster0.dfca3fo.mongodb.net/?retryWrites=true&w=majority"
MONGO_CONN=pymongo.MongoClient(MONGO_URI)

def conn_mongodb(): # return mongodb DATABASE
    db=MONGO_CONN.online_store # with mongo client, add "online store" database to cluster(?)
    # test_connection=db.test_connection.insert_one({'test': 'test'}) # insert the collection
    return db 

# conn_mongodb()

# mongodb compass download 221108 (complete)
# CRUD learning (complete)
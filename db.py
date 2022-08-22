import urllib
import urllib.parse.quote


def get_database():
    import pymongo
    from pymongo import MongoClient, InsertOne
    
    CONNECTION_STRING = f"mongodb+srv://harmeshverma01: {urllib.quote('<password>Verma@098')}@cluster0.oebmycg.mongodb.net/?retryWrites=true&w=majority"
    
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['product']


if __name__ == "__main__":
    
    dbname = get_database()
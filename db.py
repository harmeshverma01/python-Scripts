# import urllib.parse
# from pymongo import MongoClient


# def get_database():
#     username = urllib.parse.quote_plus('harmeshverma01')
#     password = urllib.parse.quote_plus('Verma@098')
#     CONNECTION_STRING = "mongodb+srv://{0}:{1}@cluster0.oebmycg.mongodb.net/?retryWrites=true&w=majority".format(username, password)
#     cluster = MongoClient(CONNECTION_STRING)
#     db = cluster['Product']
#     dblist = cluster.list_database_names()
#     print("HNJHH: ", dblist)
#     return db

# if __name__ == "__main__":
    
#     dbname = get_database()
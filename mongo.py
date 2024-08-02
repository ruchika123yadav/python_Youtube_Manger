from pymongo import MongoClient

uri = "mongodb+srv://youtubepy:youtubePy@cluster0.n1opmb4.mongodb.net/ytmanager?retryWrites=true&w=majority&authSource=admin"
client = MongoClient(uri, tlsAllowInvalidCertificates=True)

db = client.ytmanager
print("Databases:", client.list_database_names())
print("Collections in ytmanager:", db.list_collection_names())

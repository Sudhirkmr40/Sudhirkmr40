import pymongo

client = pymongo.MongoClient("mongodb+srv://Tonystark:Jarvis@cluster0.8k157.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

data2 = {"name" : "tonystark", "surname": "iron man" , "profile": "nuclear weapon scientist"}
database = client['myinfo']
collection = database["sudhir"]
collection.insert_one(data2)

New_records = [
 {"name" : "tonystark", "surname": "iron man" , "profile": "nuclear weapon scientist"},
 {"name" : "chris", "surname": "hemsworth" , "profile": "thor"},
{"name" : "ethan", "surname": "hunt" , "profile": "MIA"}]
database = client['myinfo']
collection = database["New_records"]
collection.insert_many(New_records)



import datetime

d = datetime.datetime.now(datetime.timezone.utc).isoformat()

print(d)












# import pymongo

# from src.api.models.user import User

# client = pymongo.MongoClient(
#     host="localhost", port=27017, username="root", password="example"
# )
# db = client.test

# user = User(id=1)
# print(user.id)
# print(user.plus())



# # print(db.name)

# # db.my_collection
# # print(db.my_collection.insert_one({"x": 10}).inserted_id)
# # db.my_collection.insert_one({"x": 8}).inserted_id
# # db.my_collection.insert_one({"x": 11}).inserted_id
# # print(db.my_collection.find_one())

# # for item in db.my_collection.find():
# #     print(item["x"])

# # db.my_collection.create_index("x")

# # for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
# #     print(item["x"])

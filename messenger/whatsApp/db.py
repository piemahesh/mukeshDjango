from pymongo import MongoClient


mongoLink = MongoClient("mongodb://localhost:27017")
DataBase = mongoLink.mukeshDb #database
userCol = DataBase.users
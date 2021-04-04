import pymongo

class Mongodb:

    def __init__(self,url,db,col):
        self.client = pymongo.MongoClient(url)
        self.db = self.client[db]
        self.col = self.db[col]

    def findWithParams(self,select,params):
        response = self.col.find(select,params)
        return response

    def select_one(self): #uno simple       
        doc = self.col.find_one({}).pretty()
        return doc

    def ultimoDato(self): #ultimo Dato
        doc = self.col.find_one({"$query":{}, "$orderby":{"$natural":-1}})
        return doc

    def varios(self): #varios
        resultados = self.col.find({})
        return resultados

    def insertar(self, data): #insertar
        self.col.insert_one(data)
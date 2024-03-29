from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings

class SalaRepository:
    def __init__(self):
        self.client = MongoClient(getattr(settings, "MONGO_CONNECTION_STRING"))
        self.db = self.client[getattr(settings, "MONGO_DATABASE_NAME")]
        self.collection = self.db['sala']

    def listar_todas(self):
        return list(self.collection.find())

    def obter_por_id(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def criar_sala(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def atualizar_sala(self, id, data):
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return result.modified_count > 0

    def excluir_sala(self, id):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

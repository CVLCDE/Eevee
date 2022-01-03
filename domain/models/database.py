from pymongo import MongoClient
from flask_pymongo import PyMongo
from domain.config.config import Config

mongo = PyMongo()


class EEVEE_DB(object):
    def __init__(self):
        self.db = mongo.db

    def get_all_cards(self, collection):
        return [document for document in self.db[collection].find({})]

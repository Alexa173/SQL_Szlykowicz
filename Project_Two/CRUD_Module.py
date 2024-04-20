# Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #s

        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31287
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.collection.insert_one(data)  # data should be dictionary
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            


# Create method to implement the R in CRUD.
    def read(self,readData):
        if readData is not None:
            data = self.collection.find(readData, {"_id": False})
        else:
            data = self.collection.find({}, {"_id": False})
        
        return data


#Create method to implement the U in CRUD
# changed_result = self.database.animals.update_many(searched, {"$set": changed})
    def update(self, updateData):
        if updateData is not None:
            if updateData :
                result = self.collection.update_many(updateData)
                return result
        else:
            raise Exception("Nothing to update, because data parameter is empty")


    def delete(self, deleteData):
        if deleteData is not None:
            if deleteData :
                result = self.collection.delete_one(deleteData)
                return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")

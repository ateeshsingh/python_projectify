

class DbFunctions:

    @staticmethod
    def find_all(database,collection_name,query,projection):
        return list(database.get_collection(collection_name).find(query,projection))





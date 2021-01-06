from pymongo import MongoClient


class MongoDBConnection:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            "mongodb+srv://mukulmantosh:9fRIqCFZ1hA9RLE4@mydb.6q0tq.mongodb.net/myDB?retryWrites=true&w=majority")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

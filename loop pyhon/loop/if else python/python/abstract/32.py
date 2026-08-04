# 32. Database Interface

# Methods:

# connect()
# disconnect()

# Implement:

# MySQL
# MongoDB
# PostgreSQL

import abc
class DatabaseInterface(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass
    
class MySQL(DatabaseInterface):
    def connect(self):
        print("Connecting to MySQL database...")

    def disconnect(self):
        print("Disconnecting from MySQL database...")   
        
class MongoDB(DatabaseInterface):
    def connect(self):
        print("Connecting to MongoDB database...")

    def disconnect(self):
        print("Disconnecting from MongoDB database...")     
        
class PostgreSQL(DatabaseInterface):
    def connect(self):
        print("Connecting to PostgreSQL database...")

    def disconnect(self):
        print("Disconnecting from PostgreSQL database...")  
        
mysql_db = MySQL()
mysql_db.connect()
mysql_db.disconnect()   

mongo_db = MongoDB()
mongo_db.connect()
mongo_db.disconnect()   

postgres_db = PostgreSQL()
postgres_db.connect()
postgres_db.disconnect()   
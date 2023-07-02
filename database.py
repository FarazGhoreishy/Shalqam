import mysql.connector
import config

class Database:
    def __init__(self) -> None:
        self.database = mysql.connector.connect(**config.database_config)  

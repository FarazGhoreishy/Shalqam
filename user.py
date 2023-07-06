import hashlib
import mysql
from database import Database
from item import Item

class User:

    def __init__(self, user_id, first_name, last_name, username, email):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    @classmethod
    def login(cls, username, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        db = Database()
        cursor = db.database.cursor()

        query = "SELECT user_id, first_name, last_name, username, email FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, [username, hashed_password])
        user_info = cursor.fetchone()
        cursor.close()
        db.database.close()
        
        if user_info is None or user_info[0] is None:
                raise ValueError("Invalid Login Credentials")

               
        user = cls(*user_info)
        return user
    
    @classmethod
    def signup(cls, first_name, last_name, username, email, password, repeat_password):
        if not User.password_validation(password, repeat_password):
            raise ValueError("Passwords dont match")
        
        if not User.user_info_validation(first_name, last_name, username, email):
            raise ValueError("Invalid SignUp Credentials")
        
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        db = Database()
        cursor = db.database.cursor()
        query = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, [username, hashed_password, first_name, last_name, email])
            db.database.commit()
        except mysql.connector.errors.IntegrityError:
            raise ValueError("This Username is taken")
        
        cursor.close()
        db.database.close()

        user = cls(cursor.lastrowid, first_name, last_name, username, email)
        return user
    
    @staticmethod
    def password_validation(password, repeatpassword):
        return password == repeatpassword
    
    @staticmethod
    def user_info_validation(*args):
        for arg in args:
            if len(arg) == 0:
                return False
        return True

    def __str__(self) -> str:
        return f"User({self.username}, {self.user_id})"

    def __repr__(self) -> str:
        return f"User({self.username}, {self.user_id})"
    
    def getFavorites(self):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT item_id FROM favorites WHERE user_id = %s"
        cursor.execute(query, [self.user_id])
        item_ids = cursor.fetchall()
        
        favorite_items = []
        for item_id in item_ids:
            favorite_items.append(Item.load(item_id[0]))
        
        return favorite_items

    def addFavorite(self, item_id):
        db = Database()
        cursor = db.database.cursor()
        query = "INSERT INTO favorites (user_id, item_id) VALUES (%s, %s)"
        
        print("user_id, item_id", self.user_id, item_id)

        cursor.execute(query, [self.user_id, item_id])

        db.database.commit()
        cursor.close()
        db.database.close()
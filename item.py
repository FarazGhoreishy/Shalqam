from database import Database

class Item:

    def __init__(self, item_id, name, category):
        self.item_id = item_id
        self.name = name
        self.category = category

    @classmethod
    def register(cls, name, category, links):
        db = Database()
        cursor = db.database.cursor()
        query = "INSERT INTO items (name, category) VALUES (%s, %s)"
        cursor.execute(query, [name, category])
        db.database.commit()
        item_id = cursor.lastrowid

        for link in links:
            query = "INSERT INTO links (item_id, link) VALUES (%s, %s)"
            cursor.execute(query, [item_id, link])
        
        db.database.commit()
        cursor.close()
        db.database.cloes()
        
        item = cls(item_id, name, category)
        return item
    
    @classmethod
    def load(cls, item_id):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT * FROM items WHERE item_id = %s"
        cursor.execute(query, [item_id])
        item_info = cursor.fetchone()

        if item_info is None:
            raise ValueError("No such item exists")
        
        item = cls(*item_info)
        return item

    def __str__(self) -> str:
        return f"Item({self.name}, {self.item_id})"

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.item_id})" 
    
    def getLinks(self):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT link FROM links WHERE item_id = %s"
        cursor.execute(query, [self.item_id])
        links = cursor.fetchall()
        
        return links
    
    @property
    def price(self):
        return 100
    
    def getImage(self):
        return "ui\\resources/placeholder.png"
    

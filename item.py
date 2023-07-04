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
        query = "SELECT item_id, name, category FROM items WHERE item_id = %s"
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
        '''returns a list of links registered for a particular item'''
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT link FROM links WHERE item_id = %s"
        cursor.execute(query, [self.item_id])
        links = cursor.fetchall()
        
        links = [link[0] for link in links]
        return links
    
    def getImagesFromLinks(self):
        '''returns a list containing images obtained from item links'''
        links = self.getLinks()
        return ["ui\\resources/placeholder.png", "ui\\resources/placeholder.png"]

    def getPricesFromLinks(self):
        '''returns a list of prices registered for an item from links'''
        links = self.getLinks()
        return [100, 110]
    
    @property
    def price(self):
        '''returns the least price for a item from all prices available in the links'''
        return min(self.getPricesFromLinks())
    
    def getImage(self):
        '''returns an image of the item from one of the links'''
        return "ui\\resources/placeholder.png"
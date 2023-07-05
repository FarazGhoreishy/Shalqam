from database import Database
from webdriver import Webdriver
from selenium.webdriver.common.by import By
import requests

class Item:

    def __init__(self, item_id, name, category, main_link, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.main_link = main_link
        self.price = price

    @classmethod
    def register(cls, name, category, links, main_link, price):
        db = Database()
        cursor = db.database.cursor()
        query = "INSERT INTO items (name, category, main_link, price) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, [name, category, main_link, price])
        db.database.commit()
        item_id = cursor.lastrowid

        for link in links:
            query = "INSERT INTO links (item_id, link) VALUES (%s, %s)"
            cursor.execute(query, [item_id, link])
        
        db.database.commit()
        cursor.close()
        db.database.close()
        
        item = cls(item_id, name, category, main_link, price)
        return item
    
    @classmethod
    def load(cls, item_id):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT item_id, name, category, main_link, price FROM items WHERE item_id = %s"
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
        wd = Webdriver()
        wd.driver.get(self.main_link)

        shop_image_elements = wd.driver.find_elements(By.CLASS_NAME, "shop-logo")
        
        shop_images = []
        shop_names = []
        for shop_image_element in shop_image_elements:
            url = shop_image_element.get_attribute('src')
            
            shop_name = shop_image_element.get_attribute('alt')
            shop_names.append(shop_name)

            try:
                image = requests.get(url).content
            except:
                url = shop_image_element.get_attribute('data-lazysrc')
                image = requests.get(url).content

            shop_images.append(image)

        return zip(shop_images, shop_names)

    def getPricesFromLinks(self):
        '''returns a list of prices registered for an item from links'''
        wd = Webdriver()
        wd.driver.get(self.main_link)

        shop_price_elements = wd.driver.find_elements(By.CLASS_NAME, "shop-price")

        shop_prices = []
        for shop_price_element in shop_price_elements:
            shop_prices.append(shop_price_element.text)

        shop_prices = [shop_price.split('\n')[-1] for shop_price in shop_prices]
        
        wd.driver.quit()
        return shop_prices
    
   
    def getImage(self):
        '''returns an image of the item from the main link'''
        
        print("...Getting Image...")
        wd = Webdriver()
        wd.driver.get(self.main_link)

        item_image_element = wd.driver.find_element(By.ID, "ContentPlaceHolder1_rptMainSlider_ImgSlideItem_0")
        item_image_url = item_image_element.get_attribute('src')
        item_image = requests.get(item_image_url).content

        wd.driver.quit()
        print("...Got Image...")
        return item_image
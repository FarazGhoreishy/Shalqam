from selenium import webdriver
from selenium.webdriver.common.by import By

from ui_item import Ui_Dialog
from time import sleep

from PyQt5.QtWidgets import QApplication, QDialog

import requests
import sys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options = options)
driver.minimize_window()

item_link = "https://emalls.ir/%D9%85%D8%B4%D8%AE%D8%B5%D8%A7%D8%AA_%D9%85%D9%88%D8%AF%D9%85-%D9%81%DB%8C%D8%A8%D8%B1-%D9%86%D9%88%D8%B1%DB%8C-%D9%81%D8%A7%DB%8C%D8%A8%D8%B1%D9%87%D9%88%D9%85-AN5506-02FG~id~4977080"
driver.get(item_link)


category_breadcrumb = driver.find_element(By.ID, "divbreadcrumb")
category_breadcrumb = category_breadcrumb.text.split('\n')

category_name = category_breadcrumb[2]
item_name = category_breadcrumb[-1]

item_image_element = driver.find_element(By.ID, "ContentPlaceHolder1_rptMainSlider_ImgSlideItem_0")
item_image_url = item_image_element.get_attribute('src')
item_image = requests.get(item_image_url).content


shop_image_elements = driver.find_elements(By.CLASS_NAME, "shop-logo")

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

shop_links = []
for i in range(len(shop_images)):
    id = f"ContentPlaceHolder1_rptShops_hlkDescription_{i}"
    shop_link_element = driver.find_element(By.ID, id)
    shop_link_url = shop_link_element.get_attribute('href')
    shop_links.append(shop_link_url)


shop_price_elements = driver.find_elements(By.CLASS_NAME, "shop-price")

shop_prices = []
for shop_price_element in shop_price_elements:
    shop_prices.append(shop_price_element.text)

shop_prices = [shop_price.split('\n')[-1] for shop_price in shop_prices]


driver.quit()


class ItemWindow(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self, category_name, item_name, item_image, shop_images, shop_names, shop_prices)

app = QApplication(sys.argv)
win = ItemWindow()
win.show()
sys.exit(app.exec())



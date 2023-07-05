from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from item import Ui_Dialog
from time import sleep

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QLabel

import requests
import sys


search_entry = "هدفون بیسیم"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options = options)
driver.maximize_window()

item_link = "https://emalls.ir/"
driver.get(item_link)

search_box = driver.find_element(By.ID, "SearchInBottom_txtSearch")
search_box.send_keys(search_entry)
search_box.send_keys(Keys.ENTER)


sleep(10)
driver.quit()
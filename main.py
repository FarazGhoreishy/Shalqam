import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem, QLabel
from PyQt5.QtWidgets import QPushButton, QLabel

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from ui_main_window import Ui_MainWindow as Main_Ui_Window
from ui_login import Ui_Dialog as  Login_Ui_Dialog
from ui_signup import Ui_Dialog as SignUP_Ui_Dialog
from ui_category import Ui_Dialog as Category_Ui_Dialog
from ui_item import Ui_Dialog as Item_Ui_Dialog
from ui_favorites import Ui_Dialog as Favorite_Ui_Dialog
from ui_search import Ui_Dialog as Search_Ui_Dialog

from user import User
from item import Item
from database import Database
from webdriver import Webdriver
from web_functions import WebFunctions

class Window(QMainWindow, Main_Ui_Window):
    user = None

    def __init__(self, parent = None):
        super().__init__(parent)
        self.category_names = self.getCategories()
        self.setupUi(self, self.category_names)
        self.connectSignalsSlots()
        self.favorites_pushButton.hide()
        self.logout_pushButton.hide()
        self.fillCategoryTables()

    def getCategories(self):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT DISTINCT category FROM items"
        cursor.execute(query)
        categories = cursor.fetchall()
        cursor.close()
        db.database.close()

        categories = [category[0] for category in categories]
        return categories
    
    def connectSignalsSlots(self):
        self.message_pushButton.clicked.connect(self.executeLogin)
        self.login_pushButton.clicked.connect(self.executeLogin)
        self.signup_pushButton.clicked.connect(self.executeSignUp)
        self.favorites_pushButton.clicked.connect(self.executeFavorites)
        self.logout_pushButton.clicked.connect(self.executeLogout)
        self.search_pushButton.clicked.connect(self.executeSearch)

        for i in range(len(self.action_categories)):
            category_name = self.category_names[i]
            self.action_categories[i].triggered.connect(self.createCategoryFucntion(category_name))
    
    def executeLogin(self):
        dialog = LoginDialog()
        dialog.exec()

        if Window.user is not None:
            self.message_pushButton.setText(f"Hello {Window.user.first_name}, welcome!")
            self.login_pushButton.hide()
            self.signup_pushButton.hide()
            self.favorites_pushButton.show()
            self.logout_pushButton.show()

    def executeSignUp(self):
        dialog = SignUpDialog()
        dialog.exec()

    def executeLogout(self):
        msg = QMessageBox()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)

        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Shalqam - Logout")
        msg.setText("Are you sure you want to logout?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        reply = msg.exec()
        
        if reply == QMessageBox.Ok:
            Window.user = None
            self.message_pushButton.setText("Login to save your favorite items!")
            self.login_pushButton.show()
            self.signup_pushButton.show()
            self.favorites_pushButton.hide()
            self.logout_pushButton.hide()

    def fillCategoryTables(self):
        
        for i in range(len(self.category_tableWidgets)):
            category_name = self.category_names[i]
            category_tableWidget = self.category_tableWidgets[i]
            
            items = CategoryWindow.getItems(category_name)

            label_font = QtGui.QFont()
            label_font.setFamily("Josefin Slab")
            label_font.setPointSize(16)
            
            for column_number, item in enumerate(items):
                if column_number == 10:
                    break
                
                # insert item name
                item_name_button = QPushButton()
                item_name_button.setFont(label_font)
                item_name_button.setStyleSheet("QPushButton{ border-style: none;  text-align: center}")
                item_name_button.setText(item.name)
                
                category_tableWidget.setCellWidget(0, column_number, item_name_button)

                item_name_button.clicked.connect(self.createItemFunction(item.name))

                # insert item image
                item_image_label = QLabel()

                item_pixmap = QtGui.QPixmap()
                item_pixmap.loadFromData(item.getImage())
                item_image_label.setPixmap(item_pixmap.scaled(180, 180))
                item_image_label.setAlignment(Qt.AlignCenter)
                category_tableWidget.setCellWidget(1, column_number, item_image_label)

                # insert item price
                price_entry = QTableWidgetItem(item.price)
                price_entry.setTextAlignment(Qt.AlignCenter)
                price_entry.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                category_tableWidget.setItem(2, column_number, price_entry)

            # category_tableWidget.resizeRowsToContents() 
            category_tableWidget.horizontalHeader().setDefaultSectionSize(180)
            category_tableWidget.verticalHeader().setDefaultSectionSize(180)

    def executeFavorites(Self):
        dialog = FavoriteWindow()
        dialog.exec()

    def createCategoryFucntion(self, category_name):

        def executeCategory(self):
            dialog = CategoryWindow(category_name)
            dialog.exec()

        return executeCategory
    
    def createItemFunction(self, item_name):

        def executeItem(self):
            dialog = ItemWindow(item_name)
            dialog.exec()

        return executeItem
    
    def executeSearch(self):
        search_entry = self.search_lineEdit.text()
        items = WebFunctions.search_web(search_entry)

        dialog = SearchWindow(search_entry, items)
        dialog.exec()
        
class LoginDialog(QDialog, Login_Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.login_pushButton.clicked.connect(self.checkLogin)
        self.signup_pushButton.clicked.connect(Window.executeSignUp)

    def checkLogin(self):

        user_inputs = [
            self.username_lineEdit.text(),
            self.password_lineEdit.text()
        ]

        try:
            Window.user = User.login(*user_inputs)
            self.close()
        
        except ValueError as error_message:
            msg = QMessageBox()

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Login Error")
            msg.setText(str(error_message))
            msg.exec()

class SignUpDialog(QDialog, SignUP_Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.signup_pushButton.clicked.connect(self.checkSignUp)

    def checkSignUp(self):
        user_inputs = [
            self.firstName_lineEdit.text(),
            self.lastName_lineEdit.text(),
            self.username_lineEdit.text(),
            self.email_lineEdit.text(),
            self.password_lineEdit.text(),
            self.repeatPassword_lineEdit.text()
        ]

        try:
            user = User.signup(*user_inputs)
        
        except ValueError as error_message:
            msg = QMessageBox()

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("SignUp Error")
            msg.setText(str(error_message))
            msg.exec()

class CategoryWindow(QDialog, Category_Ui_Dialog):
    def __init__(self, category_name, parent = None):
        super().__init__(parent)
        self.category_name = category_name
        self.items = CategoryWindow.getItems(self.category_name)
        self.setupUi(self, category_name, self.items)
    
    @staticmethod
    def getItems(category_name):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT item_id FROM items WHERE category = %s"
        cursor.execute(query, [category_name])
        items = cursor.fetchall()
        cursor.close()
        db.database.close()

        item_ids = [item[0] for item in items]
        items = [Item.load(item_id) for item_id in item_ids]
        return items

class ItemWindow(QDialog, Item_Ui_Dialog):
    def __init__(self, item_name, parent = None):
        super().__init__(parent)
        self.item_name = item_name
        self.createTableInfo()
        self.setupUi(self, self.item.category, item_name, self.item.getImage(), self.image_list, self.links, self.price_list)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.favorite_pushButton.clicked.connect(self.executeFavorite)
        
        for index, item_link_button in enumerate(self.item_link_buttons):
            item_link_button.clicked.connect(self.createWebpageFunction(self.links[index], index))

    def createTableInfo(self):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT item_id, name, category, main_link, price FROM items WHERE name = %s"
        cursor.execute(query, [self.item_name])
        item_info = cursor.fetchone()
        
        self.item = Item(*item_info)

        self.links = self.item.getLinks()
        self.image_list = self.item.getImagesFromLinks()
        self.price_list = self.item.getPricesFromLinks()

    def executeFavorite(self):

        if Window.user is None:
            msg = QMessageBox()

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)

            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Shalqam - User Error")
            msg.setText("You Need to Login to Save Your Favorites.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

        else:
            Window.user.addFavorite(self.item.item_id)
            print("Successful?", Window.user)

    def createWebpageFunction(self, link, index):

        def openPage():
            wd = Webdriver()
            wd.driver.get(link)
            wd.driver.maximize_window()
            buttons = wd.driver.find_elements(By.LINK_TEXT, "خرید اینترنتی")
            # print("count :", len(buttons))
            # buttons[index].click()

            # actions = ActionChains(wd.driver)
            # actions.move_to_element(buttons[index]).perform()
            # buttons[index].click()
            wd.driver.get(buttons[index].get_attribute('href'))


        return openPage

class FavoriteWindow(QDialog, Favorite_Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self, Window.user, Window.user.getFavorites())

class SearchWindow(QDialog, Search_Ui_Dialog):
    def __init__(self, search_entry, items, parent = None):
        super().__init__(parent)
        self.setupUi(self, search_entry, items)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

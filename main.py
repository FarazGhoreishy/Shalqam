import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QStackedWidget
from PyQt5.uic import loadUi

from ui_main_window import Ui_MainWindow as Main_Ui_Window
from ui_login import Ui_Dialog as  Login_Ui_Dialog
from ui_signup import Ui_Dialog as SignUP_Ui_Dialog
from ui_category import Ui_Dialog as Category_Ui_Dialog

from user import User
from item import Item
from database import Database

class Window(QMainWindow, Main_Ui_Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.category_names = self.getCategories()
        self.setupUi(self, self.category_names)
        self.connectSignalsSlots()
        self.favorites_pushButton.hide()
        self.logout_pushButton.hide()
        

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
        
        for i in range(len(self.action_categories)):
            category_name = self.category_names[i]
            self.action_categories[i].triggered.connect(self.createCategoryFucntion(category_name))
    
    def executeLogin(self):
        dialog = LoginDialog()
        dialog.exec()
        # self.loginMessage_pushButton.clicked.connect(lambda : print("Hello"))
        
    def executeSignUp(self):
        dialog = SignUpDialog()
        dialog.exec()

    def createCategoryFucntion(self, category_name):

        def executeCategory(self):
            dialog = CategoryWindow(category_name)
            dialog.exec()

        return executeCategory
    
class LoginDialog(QDialog, Login_Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.login_pushButton.clicked.connect(self.checkLogin)
        self.signup_pushButton.clicked.connect(self.executeSignUp)

    def checkLogin(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        user = User.login(username, password)
        print(user)
        
    def executeSignUp(self):
        dialog = SignUpDialog()
        dialog.exec()

class SignUpDialog(QDialog, SignUP_Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.signup_pushButton.clicked.connect(self.checkSignUp)

    def checkSignUp(self):
        pass

class CategoryWindow(QDialog, Category_Ui_Dialog):
    def __init__(self, category_name, parent = None):
        super().__init__(parent)
        self.category_name = category_name
        self.setupUi(self, category_name, self.getItems())

        
    def getItems(self):
        db = Database()
        cursor = db.database.cursor()
        query = "SELECT item_id FROM items WHERE category = %s"
        cursor.execute(query, [self.category_name])
        items = cursor.fetchall()
        cursor.close()
        db.database.close()

        item_ids = [item[0] for item in items]
        items = [Item.load(item_id) for item_id in item_ids]
        print(items)
        return items
    
    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

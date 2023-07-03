import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow as Main_Ui_Window
from ui_login import Ui_Dialog as  Login_Ui_Dialog
from ui_signup import Ui_Dialog as SignUP_Ui_Dialog
from ui_category import Ui_Dialog as Category_Ui_Dialog

from user import User
from item import Item
from database import Database

class Window(QMainWindow, Main_Ui_Window):
    user = None

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
        self.favorites_pushButton.clicked.connect(self.showFavorites)
        self.logout_pushButton.clicked.connect(self.executeLogout)

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

    def showFavorites(Self):
        pass

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
        self.signup_pushButton.clicked.connect(Window.executeSignUp)

    def checkLogin(self):

        user_inputs = [
            self.username_lineEdit.text(),
            self.password_lineEdit.text()
        ]

        try:
            Window.user = User.login(*user_inputs)
            print(Window.user)
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
            print(user)
        
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

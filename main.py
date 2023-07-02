import sys
import pickle
import bcrypt
import mysql.connector

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from ui_main_window import Ui_MainWindow
from ui_login import Ui_Dialog as  Login_Ui_Dialog
from ui_signup import Ui_Dialog as SignUP_Ui_Dialog
from user import User
from database import Database

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self, self.getCategories())
        self.connectSignalsSlots()
        

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
        self.login_pushButton.clicked.connect(self.executeLogin)
        self.loginMessage_pushButton.clicked.connect(self.executeLogin)
        self.signup_pushButton.clicked.connect(self.executeSignUp)
    
    def executeLogin(self):
        dialog = LoginDialog()
        dialog.exec()
        # self.loginMessage_pushButton.clicked.connect(lambda : print("Hello"))
        
    def executeSignUp(self):
        dialog = SignUpDialog()
        dialog.exec()


class LoginDialog(QDialog, Login_Ui_Dialog):
    def __init__(self, parent=None):
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.signup_pushButton.clicked.connect(self.checkSignUp)

    def checkSignUp(self):
        pass


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

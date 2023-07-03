from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, categories):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(860, 770)

        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(14)
        MainWindow.setFont(font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.shalqam_label = QtWidgets.QLabel(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shalqam_label.sizePolicy().hasHeightForWidth())

        self.shalqam_label.setSizePolicy(sizePolicy)
        self.shalqam_label.setMaximumSize(QtCore.QSize(30, 30))
        self.shalqam_label.setText("")
        self.shalqam_label.setPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"))
        self.shalqam_label.setScaledContents(True)
        self.shalqam_label.setObjectName("shalqam_label")

        self.horizontalLayout_2.addWidget(self.shalqam_label)

        self.message_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(22)
        self.message_pushButton.setFont(font)
        self.message_pushButton.setStyleSheet("QPushButton{border-radius: 0px; border-style: none;}")
        self.message_pushButton.setObjectName("message_pushButton")
        self.horizontalLayout_2.addWidget(self.message_pushButton)

        self.login_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.login_pushButton.setFont(font)
        self.login_pushButton.setStyleSheet("QPushButton{ padding: 0 20px; width: 100%; height: 50px; background-color: #57b846; border-radius: 25px; color: #fff; line-height: 1.2;}")
        self.login_pushButton.setObjectName("login_pushButton")

        self.favorites_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.favorites_pushButton.setFont(font)
        self.favorites_pushButton.setStyleSheet("QPushButton{ padding: 0 20px; width: 100%; height: 50px; background-color: #57b846; border-radius: 25px; color: #fff; line-height: 1.2;}")
        self.favorites_pushButton.setObjectName("favorites_pushButton")

        # self.stackedWidget_1 = QtWidgets.QStackedWidget(self.centralwidget)
        # self.stackedWidget_1.addWidget(self.login_pushButton)
        # self.stackedWidget_1.addWidget(self.favorites_pushButton)
        # self.stackedWidget_1.setCurrentIndex(1)

        # self.horizontalLayout_2.addWidget(self.stackedWidget_1)

        self.horizontalLayout_2.addWidget(self.login_pushButton)
        self.horizontalLayout_2.addWidget(self.favorites_pushButton)
        
        self.signup_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.signup_pushButton.setFont(font)
        self.signup_pushButton.setStyleSheet("QPushButton{ padding: 0 20px; width: 100%; height: 50px; background-color: #57b846; border-radius: 25px; color: #fff; line-height: 1.2;}")
        self.signup_pushButton.setObjectName("signup_pushButton")

        self.logout_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.logout_pushButton.setFont(font)
        self.logout_pushButton.setStyleSheet("QPushButton{ padding: 0 20px; width: 100%; height: 50px; background-color: #57b846; border-radius: 25px; color: #fff; line-height: 1.2;}")
        self.logout_pushButton.setObjectName("logout_pushButton")

        # self.stackedWidget_2 = QtWidgets.QStackedWidget(self.centralwidget)
        # self.stackedWidget_2.addWidget(self.signup_pushButton)
        # self.stackedWidget_2.addWidget(self.logout_pushButton)
        # self.stackedWidget_2.setCurrentIndex(1)

        # self.horizontalLayout_2.addWidget(self.stackedWidget_2)
        self.horizontalLayout_2.addWidget(self.signup_pushButton)
        self.horizontalLayout_2.addWidget(self.logout_pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(16)
        self.scrollArea.setFont(font)

        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 1200))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 1200))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.search_pushButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.search_pushButton.setFont(font)
        self.search_pushButton.setStyleSheet("")
        self.search_pushButton.setObjectName("search_pushButton")
        self.horizontalLayout.addWidget(self.search_pushButton)

        self.search_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.search_lineEdit.setFont(font)
        self.search_lineEdit.setStyleSheet("")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.horizontalLayout.addWidget(self.search_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        
        self.category_labels = []
        self.category_tableWidgets = []
        self.category_names = categories

        for category in categories:
                category_label = QtWidgets.QLabel(self.frame)

                font = QtGui.QFont()
                font.setFamily("HoloLens MDL2 Assets")
                font.setPointSize(16)

                category_label.setFont(font)
                category_label.setLayoutDirection(QtCore.Qt.LeftToRight)
                category_label.setAutoFillBackground(False)
                category_label.setObjectName(f"{category}_label")

                category_tableWidget = QtWidgets.QTableWidget(self.frame)
                category_tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
                category_tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                category_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
                category_tableWidget.setShowGrid(True)
                category_tableWidget.setObjectName(f"{category}_tableWidget")
                category_tableWidget.setColumnCount(10)
                category_tableWidget.setRowCount(3)


                for i in range(3):
                     item = QtWidgets.QTableWidgetItem()
                     category_tableWidget.setVerticalHeaderItem(i, item)
                

                for i in range(10):
                     item = QtWidgets.QTableWidgetItem()
                     category_tableWidget.setHorizontalHeaderItem(i, item)

                category_tableWidget.horizontalHeader().setVisible(True)
                category_tableWidget.verticalHeader().setVisible(True)

                self.category_labels.append(category_label)
                self.category_tableWidgets.append(category_tableWidget)


                self.verticalLayout_3.addWidget(self.category_labels[-1])
                self.verticalLayout_3.addWidget(self.category_tableWidgets[-1])
        
        
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 29))
        self.menubar.setObjectName("menubar")
        self.menuCategories = QtWidgets.QMenu(self.menubar)
        self.menuCategories.setObjectName("menuCategories")
        MainWindow.setMenuBar(self.menubar)
        

        self.action_categories = []

        for category in categories:
                action_category = QtWidgets.QAction(MainWindow)
                font = QtGui.QFont()
                font.setFamily("Josefin Slab")
                font.setPointSize(14)
                action_category.setFont(font)
                action_category.setObjectName(f"action_category_{category}")

                self.action_categories.append(action_category)
        
        for i in range(len(categories)):
                self.menuCategories.addAction(self.action_categories[i])
  
        self.menubar.addAction(self.menuCategories.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shalqam - Shopping Assistant"))

        self.message_pushButton.setText(_translate("MainWindow", "Login to save your favorite items!"))
        
        self.login_pushButton.setText(_translate("MainWindow", "Login"))
        self.favorites_pushButton.setText(_translate("MainWindow", "Favorites"))

        self.signup_pushButton.setText(_translate("MainWindow", "SignUp"))
        self.logout_pushButton.setText(_translate("MainWindow", "Logout"))

        self.search_pushButton.setText(_translate("MainWindow", ""))

        for i in range(len(self.category_labels)):
                self.category_labels[i].setText(_translate("MainWindow", f" {self.category_names[i]}"))
                
                headers = ["modelName", "image", "price"]
                for j in range(3):
                     item = self.category_tableWidgets[i].verticalHeaderItem(j)
                     item.setText(_translate("MainWindow", headers[j]))

                
                for j in range(10):
                     item = self.category_tableWidgets[i].horizontalHeaderItem(j)
                     item.setText(_translate("MainWindow", f"Model {j}"))

        self.menuCategories.setTitle(_translate("MainWindow", "Categories"))

        for i in range(len(self.action_categories)):
                self.action_categories[i].setText(_translate("MainWindow", f"{self.category_names[i]}"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

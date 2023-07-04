from PyQt5 import QtCore, QtGui, QtWidgets
from math import ceil

class Ui_Dialog(object):
    def setupUi(self, Dialog, category_name, items):
        _translate = QtCore.QCoreApplication.translate

        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(860, 770)
        Dialog.setWindowTitle(_translate("Dialog", "Shalqam - Category Page"))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # font setting for name buttons and labels
        label_font = QtGui.QFont()
        label_font.setFamily("Josefin Slab")
        label_font.setPointSize(18)

        # Creating category label at the top of the page
        self.category_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.category_label.setFont(font)
        self.category_label.setStyleSheet("QLabel{ width: 100%; height: 55px; background-color: #CA80DC; border-radius: 15px; padding: 0 35px 0 35px; color: #fff; line-height: 1.2;}")
        self.category_label.setAlignment(QtCore.Qt.AlignCenter)
        self.category_label.setObjectName("category_label")
        self.category_label.setText(_translate("Dialog", category_name))

        self.verticalLayout.addWidget(self.category_label)

        # Scroll area definition
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 600, 560))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        # Creating grid layout for items
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(400)

        self.item_name_buttons = []
        
        cols = 4
        rows = ceil(len(items) / cols)
        positions = [(i, j) for i in range(rows) for j in range(cols)]

        for (position, item) in zip(positions, items):
            verticalLayout = QtWidgets.QVBoxLayout()
            
            item_name_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
            item_name_button.setFont(label_font)
            item_name_button.setStyleSheet("QPushButton{ border-style: none;  text-align: center}")
            item_name_button.setText(item.name)
            
            item_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            item_label.setPixmap(QtGui.QPixmap(item.getImage()).scaled(170, 230))
            item_label.setAlignment(QtCore.Qt.AlignCenter)

            item_price_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            item_price_label.setFont(label_font)
            item_price_label.setText(_translate("Dialog", str(item.price)))
            item_price_label.setAlignment(QtCore.Qt.AlignCenter)

            verticalLayout.addWidget(item_name_button)
            verticalLayout.addWidget(item_label)
            verticalLayout.addWidget(item_price_label)

            self.gridLayout.addLayout(verticalLayout, *position)
            self.item_name_buttons.append(item_name_button)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

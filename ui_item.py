from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog, item_name, images, links, prices):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(860, 770)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.item_label = QtWidgets.QLabel(Dialog)

        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(28)
        font.setBold(True)

        self.item_label.setFont(font)
        self.item_label.setStyleSheet("QLabel{ width: 100%; height: 55px; background-color: #CA80DC; border-radius: 15px; padding: 0 35px 0 35px; color: #fff; line-height: 1.2;}")
        self.item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label.setObjectName("item_label")
        self.verticalLayout.addWidget(self.item_label)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setObjectName("tableWidget")

        label_font = QtGui.QFont()
        label_font.setFamily("Josefin Slab")
        label_font.setPointSize(16)

        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        
        self.item_link_buttons = []
        for row_number, link in enumerate(links):
            self.tableWidget.insertRow(row_number)

            item_image_label = QtWidgets.QLabel()
            item_image_label.setPixmap(QtGui.QPixmap(images[row_number]).scaled(120, 160))
            item_image_label.setAlignment(Qt.AlignCenter)

            item_link_button = QtWidgets.QToolButton()
            item_link_button.setFont(label_font)
            item_link_button.setStyleSheet("QPushButton{ border-style: none;  text-align: center}")
            item_link_button.setText(link)
            self.item_link_buttons.append(item_link_button)

            item_price_entry = QtWidgets.QTableWidgetItem(str(prices[row_number]))
            item_price_entry.setTextAlignment(Qt.AlignCenter)
            item_price_entry.setFont(label_font)
            item_price_entry.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)

            self.tableWidget.setCellWidget(row_number, 0, item_image_label)
            self.tableWidget.setCellWidget(row_number, 1, item_link_button)
            self.tableWidget.setItem(row_number, 2, item_price_entry)

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(270)
        self.verticalLayout.addWidget(self.tableWidget)


        self.favorite_pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.favorite_pushButton.setFont(font)
        self.favorite_pushButton.setStyleSheet("QPushButton{ padding: 0 20px; width: 100%; height: 50px; background-color: #57b846; border-radius: 25px; color: #fff; line-height: 1.2;}")
        self.favorite_pushButton.setObjectName("favorite_pushButton")
        self.verticalLayout.addWidget(self.favorite_pushButton)

        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shalqam - Item Page"))
        self.item_label.setText(_translate("Dialog", f"{item_name}"))
        self.favorite_pushButton.setText(_translate("Dialog", "Add to Favorites"))
        QtCore.QMetaObject.connectSlotsByName(Dialog)       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()

    images = ['ui\\resources/placeholder.png', 'ui\\resources/placeholder.png']
    links = ["'faraz_link_1'", "'faraz_link_2'"]
    prices = [100, 110]


    ui.setupUi(Dialog, "faraz", images, links, prices)
    Dialog.show()
    sys.exit(app.exec_())

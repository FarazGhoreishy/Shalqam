from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(860, 770)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/shalqam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.item_label = QtWidgets.QLabel(Dialog)
        self.item_label.setGeometry(QtCore.QRect(9, 9, 841, 91))
        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.item_label.setFont(font)
        self.item_label.setStyleSheet("QLabel{ width: 100%; height: 55px; background-color: #CA80DC; border-radius: 15px; padding: 0 35px 0 35px; color: #fff; line-height: 1.2;}")
        self.item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label.setObjectName("item_label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 841, 651))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shalqam - Item Page"))
        self.item_label.setText(_translate("Dialog", "item"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

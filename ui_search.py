from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(860, 770)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.search_result_label = QtWidgets.QLabel(Dialog)

        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        self.search_result_label.setFont(font)
        self.search_result_label.setStyleSheet("QLabel{ width: 100%; height: 55px; background-color: #57b846; border-radius: 15px; padding: 0 35px 0 35px; color: #fff; line-height: 1.2;}")
        self.search_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_result_label.setObjectName("search_result_label")

        self.verticalLayout.addWidget(self.search_result_label)

        self.item_label = QtWidgets.QLabel(Dialog)

        font = QtGui.QFont()
        font.setFamily("Josefin Slab")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        self.item_label.setFont(font)
        self.item_label.setStyleSheet("QLabel{ width: 100%; height: 55px; background-color: #CA80DC; border-radius: 15px; padding: 0 35px 0 35px; color: #fff; line-height: 1.2;}")
        self.item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label.setObjectName("item_label")

        self.verticalLayout.addWidget(self.item_label)


        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 840, 650))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.search_result_label.setText(_translate("Dialog", "Search Result"))
        self.item_label.setText(_translate("Dialog", "Search Entry"))

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

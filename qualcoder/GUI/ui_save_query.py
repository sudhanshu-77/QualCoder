# Form implementation generated from reading ui file 'ui_save_query.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogSaveQuery(object):
    def setupUi(self, DialogSaveQuery):
        DialogSaveQuery.setObjectName("DialogSaveQuery")
        DialogSaveQuery.resize(587, 443)
        DialogSaveQuery.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSaveQuery)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_name = QtWidgets.QLabel(DialogSaveQuery)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.lineEdit_name = QtWidgets.QLineEdit(DialogSaveQuery)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.label = QtWidgets.QLabel(DialogSaveQuery)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_group = QtWidgets.QLineEdit(DialogSaveQuery)
        self.lineEdit_group.setObjectName("lineEdit_group")
        self.verticalLayout.addWidget(self.lineEdit_group)
        self.label_2 = QtWidgets.QLabel(DialogSaveQuery)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(DialogSaveQuery)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 60))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 800))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogSaveQuery)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogSaveQuery)
        self.buttonBox.accepted.connect(DialogSaveQuery.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogSaveQuery.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogSaveQuery)

    def retranslateUi(self, DialogSaveQuery):
        _translate = QtCore.QCoreApplication.translate
        DialogSaveQuery.setWindowTitle(_translate("DialogSaveQuery", "Save Query"))
        self.label_name.setText(_translate("DialogSaveQuery", "Query name:"))
        self.label.setText(_translate("DialogSaveQuery", "Query Group"))
        self.label_2.setText(_translate("DialogSaveQuery", "Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSaveQuery = QtWidgets.QDialog()
    ui = Ui_DialogSaveQuery()
    ui.setupUi(DialogSaveQuery)
    DialogSaveQuery.show()
    sys.exit(app.exec())

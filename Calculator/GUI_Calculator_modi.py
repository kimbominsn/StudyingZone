# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\PythonTest\StudingZone\Calculator\GUI_Calculator_modi.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 401)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 351, 391))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 191, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_7.setDefault(False)
        self.btn_7.setObjectName("btn_7")
        self.horizontalLayout.addWidget(self.btn_7)
        self.btn_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_8.setObjectName("btn_8")
        self.horizontalLayout.addWidget(self.btn_8)
        self.btn_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_9.setObjectName("btn_9")
        self.horizontalLayout.addWidget(self.btn_9)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 191, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_4.setObjectName("btn_4")
        self.horizontalLayout_2.addWidget(self.btn_4)
        self.btn_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_5.setObjectName("btn_5")
        self.horizontalLayout_2.addWidget(self.btn_5)
        self.btn_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_6.setObjectName("btn_6")
        self.horizontalLayout_2.addWidget(self.btn_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 240, 191, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_1.setObjectName("btn_1")
        self.horizontalLayout_3.addWidget(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_2.setObjectName("btn_2")
        self.horizontalLayout_3.addWidget(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_3.setObjectName("btn_3")
        self.horizontalLayout_3.addWidget(self.btn_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 100, 61, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_divide = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        self.btn_divide.setStyleSheet("background:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_divide.setObjectName("btn_divide")
        self.verticalLayout_6.addWidget(self.btn_divide)
        self.btn_multiply = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setStyleSheet("background:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_multiply.setObjectName("btn_multiply")
        self.verticalLayout_6.addWidget(self.btn_multiply)
        self.btn_minus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setStyleSheet("background:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_minus.setObjectName("btn_minus")
        self.verticalLayout_6.addWidget(self.btn_minus)
        self.btn_plus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setStyleSheet("background:rgb(255, 255, 255);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_plus.setObjectName("btn_plus")
        self.verticalLayout_6.addWidget(self.btn_plus)
        self.btn_clear = QtWidgets.QPushButton(self.frame)
        self.btn_clear.setGeometry(QtCore.QRect(290, 50, 51, 41))
        self.btn_clear.setStyleSheet("color: rgb(109, 109, 109);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_clear.setObjectName("btn_clear")
        self.btn_delete = QtWidgets.QPushButton(self.frame)
        self.btn_delete.setGeometry(QtCore.QRect(290, 10, 51, 41))
        self.btn_delete.setStyleSheet("color: rgb(109, 109, 109);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_delete.setObjectName("btn_delete")
        self.txt_result = QtWidgets.QTextBrowser(self.frame)
        self.txt_result.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.txt_result.setStyleSheet("background-color:rgb(255, 247, 253)\n"
"")
        self.txt_result.setObjectName("txt_result")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 310, 191, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_dot = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_dot.setObjectName("btn_dot")
        self.horizontalLayout_4.addWidget(self.btn_dot)
        self.btn_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_0.setObjectName("btn_0")
        self.horizontalLayout_4.addWidget(self.btn_0)
        self.btn_is = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_is.sizePolicy().hasHeightForWidth())
        self.btn_is.setSizePolicy(sizePolicy)
        self.btn_is.setStyleSheet("background:rgb(255, 243, 244);\n"
"color: rgb(255, 0, 255);\n"
"font: 75 9pt \"한컴 고딕\";")
        self.btn_is.setObjectName("btn_is")
        self.horizontalLayout_4.addWidget(self.btn_is)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_divide.setText(_translate("MainWindow", "/"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_delete.setText(_translate("MainWindow", "<-"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_is.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

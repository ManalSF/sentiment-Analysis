# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twitter.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import img
from dataAnalysis import Analysis
from dataClean import Clean
from dataGather import Collector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 70, 371, 61))
        self.textEdit.setStyleSheet("background-color:rgba(0,0,0,50);\n"
                                    "font: 14pt \"Bauhaus 93\";\n"
                                    "border-radius:15px;\n"
                                    "border-bottom:4px bold rgba(66,66,66,255);\n"
                                    "color:rgba(255,255,255,210);\n"
                                    "padding-bottom:7px;\n"
                                    "text-size:20px;\n"
                                    "")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 160, 371, 61))
        self.textEdit_2.setStyleSheet("background-color:rgba(0,0,0,50);\n"
                                      "font: 14pt \"Bauhaus 93\";\n"
                                      "border-radius:15px;\n"
                                      "border-bottom:4px bold rgba(66,66,66,255);\n"
                                      "color:rgba(255,255,255,210);\n"
                                      "padding-bottom:7px;\n"
                                      "text-size:20px;\n"
                                      "")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 250, 131, 51))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 13pt \"Bauhaus 93\";\n"
                                      "border-color: rgb(0, 222, 163);\n"
                                      "border-color: rgb(170, 170, 255);\n"
                                      "background-color: rgb(52, 3, 108);\n"
                                      "border-radius:20px;\n"
                                      "QPushButton:#pushButton(\n"
                                      "     background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.5, fx:0.5,        fy:0.5, stop:0 rgba(0, 179, 137, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      "     color: rgba(255, 255, 255,210);\n"
                                      ");\n"
                                      "QPushButton:#pushButton:hover(\n"
                                      "     background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.5, fx:0.5,        fy:0.5, stop:0 rgba(20, 199, 157, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                      ");\n"
                                      "QPushButton:#pushButton:pressed(\n"
                                      "   padding-left:5px;\n"
                                      "   padding-top:5px;\n"
                                      "   background-color: rgba(105, 118, 132, 200);\n"
                                      ");")
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-30, -30, 561, 391))
        self.widget.setStyleSheet("image: url(:/image/twitter-g6a6077cac_1920.jpg);")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.textEdit.raise_()
        self.textEdit_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.execute)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Enter your keyword"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Enter the number of tweets"))
        self.pushButton.setText(_translate("MainWindow", "Search"))

    def execute(self):
        input1 = self.textEdit.toPlainText()
        input2 = int(self.textEdit_2.toPlainText())
        gat = Collector(input1, input2)
        gat.main()
        tw = gat.tweetList()

        cl = Clean()
        cl.main()

        ana = Analysis()
        ana.main(tw, input2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

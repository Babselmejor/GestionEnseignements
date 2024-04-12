# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 47);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 231, 491))
        self.frame.setStyleSheet("background-color: rgb(17, 112, 255);\n"
"background-color: rgb(18, 13, 47);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.icon_label = QtWidgets.QLabel(parent=self.frame)
        self.icon_label.setGeometry(QtCore.QRect(90, -10, 140, 140))
        self.icon_label.setPixmap(QtGui.QPixmap("logo.png"))
        self.icon_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line = QtWidgets.QFrame(parent=self.frame)
        self.line.setGeometry(QtCore.QRect(0, 80, 231, 21))
        self.line.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 112, 255);\n"
"background-color: rgb(18, 13, 47);\n"
"color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 100, 168, 41))
        self.commandLinkButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(10, 140, 168, 41))
        self.commandLinkButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(10, 180, 168, 41))
        self.commandLinkButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(10, 220, 168, 41))
        self.commandLinkButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(10, 420, 168, 41))
        self.commandLinkButton_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 260, 168, 41))
        self.commandLinkButton_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 100, 371, 91))
        self.textEdit.setStyleSheet("background-color: rgb(17, 112, 255);\n"
"background-color: rgb(18, 13, 47);")
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(230, 0, 531, 61))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 141, 20))
        self.label_2.setStyleSheet("\n"
"color: rgb(17, 112, 255);\n"
"color: rgb(18, 13, 47);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menufichier = QtWidgets.QMenu(parent=self.menubar)
        self.menufichier.setObjectName("menufichier")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton.setText(_translate("MainWindow", "Acceuil"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "Avis Etudiants"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "Evaluation Etudiants"))
        self.commandLinkButton_4.setText(_translate("MainWindow", "Cahier de Texte"))
        self.commandLinkButton_5.setText(_translate("MainWindow", "Deconnexion"))
        self.commandLinkButton_6.setText(_translate("MainWindow", "Rapport Mensuel"))
        self.label.setText(_translate("MainWindow", "Ecole Superieur polytechnique"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; font-style:italic; color:#ffffff;\">Bienvenue dans votre Interface </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:700; font-style:italic; color:#ffffff;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Responsable pedagogique"))
        self.menufichier.setTitle(_translate("MainWindow", "fichier"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

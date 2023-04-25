from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 618)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"border: 5px solid black;\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(203, 214, 236, 255), stop:0.50 rgba(112, 240, 238, 255), stop:1 rgba(78, 105, 212, 255));\n"
"\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1000, 600))
        self.frame.setStyleSheet("\n"
"\n"
"QTabWidget{\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid black;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(100, 149, 237);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(60, 60, 255);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"color: black;\n"
"border: 0px solid black;\n"
"background-color:rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"#label_11{\n"
"border: 2px solid black;\n"
"}\n"
"#label_12{\n"
"border: 2px solid black;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextBrowser{\n"
"border: 3px solid black;\n"
"}\n"
"\n"
"QTextEdit{\n"
"border: 3px solid black;\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"min-width: 140px;\n"
"height: 20px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: rgb(60, 60, 255);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"background-color:rgb(100, 149, 237);\n"
"}\n"
"\n"
"QTabBar::tab:pressed{\n"
"background-color: rgb(78, 105, 212);\n"
"color: rgb(255, 255, 255);\n"
"padding-border: 7px 7px 9px 7px;\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected:hover{\n"
"background: rgb(60, 60, 255);\n"
"}\n"
"\n"
"QTabWidget:pane{ \n"
"background:rgba(255, 255, 255, 0);\n"
"border:0px solid red;\n"
"margin: -10px -9px -9px -9px;\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5AFF15, stop:1 #00B712);\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar{\n"
"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QGridLayout{\n"
"border: 0px solid black;\n"
"border-radius: 0px;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: rgba(0, 0, 0 ,0);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: 2px solid black;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"background-color: qradialgradient(spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"                            stop:0 rgba(255, 0, 0, 255), \n"
"                            stop:1 rgba(64, 0, 0, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: qradialgradient(spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"                            stop:0 rgba(0, 255, 0, 255), \n"
"                            stop:1 rgba(0, 64, 0, 255));\n"
"    \n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 8, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(1, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 10, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 4, 1, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_3.addWidget(self.progressBar_2, 1, 0, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 13, 0, 1, 4)
        self._2 = QtWidgets.QGridLayout()
        self._2.setObjectName("_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._2.addItem(spacerItem4, 11, 0, 1, 3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setObjectName("checkBox_4")
        self._2.addWidget(self.checkBox_4, 10, 0, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem5, 12, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self._2.addItem(spacerItem6, 6, 0, 1, 3)
        self.label_13 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(255, 15))
        self.label_13.setObjectName("label_13")
        self._2.addWidget(self.label_13, 4, 0, 1, 3)
        self.label_14 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self._2.addWidget(self.label_14, 1, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self._2.addItem(spacerItem7, 0, 0, 1, 3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setObjectName("checkBox_2")
        self._2.addWidget(self.checkBox_2, 9, 0, 1, 3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setObjectName("checkBox_3")
        self._2.addWidget(self.checkBox_3, 7, 0, 1, 3)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self._2.addWidget(self.checkBox, 8, 0, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem8, 12, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self._2.addWidget(self.pushButton_5, 12, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self._2.addItem(spacerItem9, 3, 0, 1, 3)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self._2.addWidget(self.lineEdit_9, 2, 0, 1, 2)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(50, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self._2.addWidget(self.lineEdit_8, 5, 0, 1, 2)
        self.gridLayout_2.addLayout(self._2, 11, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(330, 350))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(10000, 10000))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_7.addWidget(self.textBrowser_2, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(330, 40))
        self.label_12.setMaximumSize(QtCore.QSize(100000, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_7, 11, 2, 1, 2)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(288, 40))
        self.label_11.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setMinimumSize(QtCore.QSize(354, 350))
        self.tabWidget_4.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.tabWidget_4.setStyleSheet("")
        self.tabWidget_4.setMovable(True)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setMinimumSize(QtCore.QSize(280, 310))
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QtCore.QSize(320, 330))
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_9.addWidget(self.textEdit_3)
        self.tabWidget_4.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(264, 20))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius: 0px;\n"
"}")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_8.addWidget(self.lineEdit_7, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(60, 20))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_8.addWidget(self.pushButton_9, 0, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem10, 1, 0, 2, 2)
        self.tabWidget_4.addTab(self.tab_6, "")
        self.verticalLayout_13.addWidget(self.tabWidget_4)
        self.gridLayout_2.addLayout(self.verticalLayout_13, 11, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem11, 12, 0, 1, 4)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_4.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Путь для скачивания отчета:</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "Готово 0/0"))
        self.checkBox_4.setText(_translate("MainWindow", "Фото с лицами "))
        self.label_13.setText(_translate("MainWindow", "Максимальноечисло данных для тепловой карты"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>За сколько дней собрать отчет</p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "Тепловая карта с подложкой"))
        self.checkBox_3.setText(_translate("MainWindow", "Оригинал фото"))
        self.checkBox.setText(_translate("MainWindow", "Тепловая карта"))
        self.pushButton_5.setText(_translate("MainWindow", "Подготовить отчет"))
        self.lineEdit_9.setText(_translate("MainWindow", "7"))
        self.lineEdit_8.setText(_translate("MainWindow", "2000"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Процесс подготовки отчета"))
        self.label_11.setText(_translate("MainWindow", "Список камер "))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), _translate("MainWindow", "Текстом"))
        self.pushButton_9.setText(_translate("MainWindow", "Обзор"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), _translate("MainWindow", "Ссылка на документ"))


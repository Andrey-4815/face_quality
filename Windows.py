from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Modal_window_quit(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_modal_window_quit()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.close)
        self.quit_2.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.quit_clicked)
        self.pushButton_4.clicked.connect(QtWidgets.QApplication.instance().quit)


    def setup_modal_window_quit(self):
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(50, 150, 320, 111))
        self.widget.setStyleSheet("QWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(225, 78, 8, 255), stop:0.55 rgba(122, 9, 123, 255), stop:0.98 rgba(39, 51, 137, 255));\n"
"border: 5px solid black;\n"
"border-radius:10px;\n"
"color: rgb(255, 255, 255);\n"
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
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 47, 85);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid black;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"border: 3px solid black;\n"
"}\n"
"\n"
"QTextEdit{\n"
"border: 3px solid black;\n"
"}\n"
"\n"
"Line{\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 70, 75, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.quit_2 = QtWidgets.QPushButton(self.widget)
        self.quit_2.setEnabled(True)
        self.quit_2.setGeometry(QtCore.QRect(275, 10, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.quit_2.setFont(font)
        self.quit_2.setMouseTracking(True)
        self.quit_2.setTabletTracking(True)
        self.quit_2.setToolTipDuration(0)
        self.quit_2.setAutoFillBackground(False)
        self.quit_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(200, 0, 0, 200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 0, 0, 220);\n"
"}")
        self.quit_2.setCheckable(False)
        self.quit_2.setObjectName("quit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(210, 70, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 301, 20))
        self.label_6.setObjectName("label_6")
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_4.setText(_translate("Dialog", "Да"))
        self.quit_2.setText(_translate("Dialog", "X"))
        self.pushButton.setText(_translate("Dialog", "Нет"))
        self.label_6.setText(_translate("Dialog", "Запущено формирование отчета, хотите остановить?"))

    def quit_clicked(self, parent):
        self.parent.Flag = False


class Modal_window(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_modal_window()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.close)
        self.quit.clicked.connect(self.close)

    def setup_modal_window(self):
        self.widget = QtWidgets.QWidget(self)
        self.widget.showMaximized()
        self.widget.setGeometry(QtCore.QRect(60, 120, 311, 111))
        self.widget.setStyleSheet("QWidget{\n"
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(225, 78, 8, 255), stop:0.55 rgba(122, 9, 123, 255), stop:0.98 rgba(39, 51, 137, 255));\n"
                                  "border: 5px solid black;\n"
                                  "border-radius:10px;\n"
                                  "color: rgb(255, 255, 255);\n"
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
                                  "}\n"
                                  "\n"
                                  "QPushButton:pressed{\n"
                                  "background-color: rgb(0, 47, 85);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "}\n"
                                  "\n"
                                  "QLabel{\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border: 0px solid black;\n"
                                  "}\n"
                                  "\n"
                                  "QLineEdit{\n"
                                  "border: 2px solid black;\n"
                                  "border-radius: 5px;\n"
                                  "}\n"
                                  "\n"
                                  "QTextBrowser{\n"
                                  "border: 3px solid black;\n"
                                  "}\n"
                                  "\n"
                                  "QTextEdit{\n"
                                  "border: 3px solid black;\n"
                                  "}\n"
                                  "\n"
                                  "Line{\n"
                                  "color:rgb(255, 255, 255)\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 75, 25))
        self.pushButton.setObjectName("pushButton")
        self.quit = QtWidgets.QPushButton(self.widget)
        self.quit.setEnabled(True)
        self.quit.setGeometry(QtCore.QRect(275, 10, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.quit.setFont(font)
        self.quit.setMouseTracking(True)
        self.quit.setTabletTracking(True)
        self.quit.setToolTipDuration(0)
        self.quit.setAutoFillBackground(False)
        self.quit.setStyleSheet("QPushButton{\n"
                                "background-color: rgb(200, 0, 0, 200);\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover{\n"
                                "background-color: rgb(220, 0, 0, 220);\n"
                                "}")
        self.quit.setCheckable(False)
        self.quit.setObjectName("quit")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 40, 291, 16))
        self.label.setObjectName("label")
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Dialog", "Ok"))
        self.quit.setText(_translate("Dialog", "X"))
        self.label.setText(_translate("Dialog", "Подождите завершения формирования прошлого отчета"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(1000, 1000)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 790, 590))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 214, 236, 255), stop:0.50 rgba(112, 240, 238, 255), stop:1 rgba(78, 105, 212, 255));\n"
"border: 5px solid black;\n"
"border-radius:10px;\n"
"color: black;\n"
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
"}\n"
"\n"
"QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QTextBrowser{\n"
"border: 3px solid black;\n"
"}\n"
"\n"
"QTextEdit{\n"
"border: 3px solid black;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
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
"QTabWidget::pane {\n"
"    border: 0px solid black;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5AFF15, stop:1 #00B712);\n"
"border-radius: 7px;\n"
"\n"
"}\n"
"\n"
"QProgressBar{\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 751, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(470, 99, 300, 451))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(160, 80, 300, 20))
        self.label.setStyleSheet("QLabel{\n"
"border: 2px solid black;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 171, 20))
        self.label_3.setObjectName("label_3")
        self.on_min = QtWidgets.QPushButton(self.groupBox)
        self.on_min.setGeometry(QtCore.QRect(720, 10, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(True)
        font.setKerning(False)
        self.on_min.setFont(font)
        self.on_min.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.on_min.setStyleSheet("")
        self.on_min.setChecked(False)
        self.on_min.setObjectName("on_min")
        self.quit = QtWidgets.QPushButton(self.groupBox)
        self.quit.setEnabled(True)
        self.quit.setGeometry(QtCore.QRect(750, 10, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.quit.setFont(font)
        self.quit.setMouseTracking(True)
        self.quit.setTabletTracking(True)
        self.quit.setFocusPolicy(QtCore.Qt.TabFocus)
        self.quit.setToolTipDuration(0)
        self.quit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.quit.setAutoFillBackground(False)
        self.quit.setStyleSheet("QPushButton{\n"
"background-color: rgb(200, 0, 0, 200);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 0, 0, 220);\n"
"}")
        self.quit.setCheckable(False)
        self.quit.setObjectName("quit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 460, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 510, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(150, 460, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(150, 510, 261, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(160, 100, 300, 330))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.textEdit = QtWidgets.QTextEdit(self.tabWidgetPage1)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 300, 300))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tabWidgetPage2)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 0, 300, 20))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius: 0px;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(470, 80, 300, 20))
        self.label_7.setStyleSheet("QLabel{\n"
"border: 2px solid black;\n"
"}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(430, 90, 30, 50))
        self.label_2.setStyleSheet("border-right: 2px solid black;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(29, 80, 121, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(20, 650, 751, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 630, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_2.raise_()
        self.tabWidget.raise_()
        self.lineEdit.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.on_min.raise_()
        self.quit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.verticalLayoutWidget.raise_()
        self.progressBar.raise_()
        self.label_8.raise_()
        self.label_8.hide()
        self.progressBar.hide()


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Проверка детектов"))
        self.label.setText(_translate("MainWindow", "Список камер "))
        self.label_3.setText(_translate("MainWindow", "Путь для скачивания отчета"))
        self.on_min.setText(_translate("MainWindow", "—"))
        self.quit.setText(_translate("MainWindow", "X"))
        self.lineEdit_2.setText(_translate("MainWindow", "7"))
        self.lineEdit_3.setText(_translate("MainWindow", "2000"))
        self.label_4.setText(_translate("MainWindow", "За сколько дней собрать отчет"))
        self.label_5.setText(_translate("MainWindow", "Максимальноечисло данных для тепловой карты"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Текстом"))
        self.lineEdit_4.setText(_translate("MainWindow", "C:\\Users\\a_grischenko\\PycharmProjects\\pythonProject3\\All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Ссылка на документ"))
        self.label_7.setText(_translate("MainWindow", "Процесс подготовки отчета"))
        self.pushButton.setText(_translate("MainWindow", "Полный отчет"))
        self.pushButton_2.setText(_translate("MainWindow", "Отчет без\n"
"тепловой карты"))
        self.pushButton_3.setText(_translate("MainWindow", "Только \n"
"тепловая карта"))
        self.label_8.setText(_translate("MainWindow", "Готово 0/0"))

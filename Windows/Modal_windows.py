from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class Modal_window_quit(QDialog):
    def __init__(self, parent=None):
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
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 214, 236, 255), stop:0.50 rgba(112, 240, 238, 255), stop:1 rgba(78, 105, 212, 255));\n"
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

    def quit_clicked(self):
        self.parent._widget.Flag = False


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
                                  "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 214, 236, 255), stop:0.50 rgba(112, 240, 238, 255), stop:1 rgba(78, 105, 212, 255));\n"
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
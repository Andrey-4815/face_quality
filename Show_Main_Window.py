import os, threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Maker import Maker
from Windows.Main_Widget import Ui_MainWindow
from Windows.Modal_windows import Modal_window


class Show_Main(Maker, QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.Flag = True
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.lineEdit_5.setText(os.getcwd())
        self.pushButton_5.clicked.connect(self.report)
        self.pushButton_9.clicked.connect(self.brows_dir)


    def brows_dir(self):
        dir, _ = QFileDialog.getOpenFileName(self, 'Select a file:', f'{os.getcwd()}')
        self.lineEdit_7.setText(dir)


    def chek_data(self):
        self.textBrowser_2.setText("")
        if not os.path.isdir(self.lineEdit_5.text()):
            self.textBrowser_2.append("Некорректный путь")
            self.lineEdit_5.setStyleSheet("QLineEdit{border: 2px solid red}")
        else:
            self.lineEdit_5.setStyleSheet("QLineEdit{border: 2px solid black}")
            self.dir = f"{self.lineEdit_5.text()}"
        if self.tabWidget_4.currentIndex() == 0:
            if self.textEdit_3.toPlainText() == "":
                self.textBrowser_2.append("Введите хотя бы один id камеры")
                self.textEdit_3.setStyleSheet("QtextEdit{border: 3px solid red}")
            else:
                self.cameras = list(set(self.textEdit_3.toPlainText().split("\n")))
        else:
            if not os.path.exists(self.lineEdit_7.text()):
                self.textBrowser_2.append("Некорректный путь до файла с камерами")
                self.lineEdit_7.setStyleSheet("QLineEdit{border: 2px solid red;border-radius: 0px}")
            else:
                if not self.lineEdit_7.text().endswith(".txt"):
                    self.textBrowser_2.append("Некорректное разрешение файла, необходимо \".txt\"")
                    self.lineEdit_7.setStyleSheet("QLineEdit{border: 2px solid red;border-radius: 0px}")
                else:
                    with open(self.lineEdit_7.text(), "r") as file:
                        self.cameras = list(set(file.read().split("\n")))
        try:
            if not int(self.lineEdit_9.text()) in range(1, 31):
                self.textBrowser_2.append("Период должен быть от 1 до 30 дней")
                self.lineEdit_9.setStyleSheet("QLineEdit{border: 2px solid red}")
            else:
                self.days = int(self.lineEdit_9.text())
                self.lineEdit_9.setStyleSheet("QLineEdit{border: 2px solid black}")
        except:
            self.textBrowser_2.append("Введите число в поле периода")
            self.lineEdit_9.setStyleSheet("QLineEdit{border: 2px solid red}")
        try:
            if not int(self.lineEdit_8.text()) in range(100, 10001):
                self.textBrowser_2.append("Количество результатов должно быть от 100 до 10000")
                self.lineEdit_8.setStyleSheet("QLineEdit{border: 2px solid red}")
            else:
                self.count_results = int(self.lineEdit_8.text())
                self.lineEdit_8.setStyleSheet("QLineEdit{border: 2px solid black}")
        except:
            self.textBrowser_2.append("Введите число в поле количчества данных")
            self.lineEdit_8.setStyleSheet("QLineEdit{border: 2px solid red}")

        if self.textBrowser_2.toPlainText() != "":
            return False
        else:
            if threading.active_count() > 1:
                Modal_window().exec_()
                return False
            else:
                self.textEdit_3.setText("")
                self.textBrowser_2.append("В работе...")
                return True


    def report(self):
        if self.chek_data():
            self.flag_orig = self.checkBox_3.checkState()
            self.flag_heat_map = self.checkBox.checkState()
            self.flag_map_with_backing = self.checkBox_2.checkState()
            self.flag_face_in_photo = self.checkBox_4.checkState()
            prep_repotr = threading.Thread(target=self.save_chart)
            prep_repotr.start()


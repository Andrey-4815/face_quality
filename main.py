import os
import threading
from PyQt5.QtCore import QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from face_quality.Prep_records import Prep_records
from face_quality.Reqests import Reqests
from face_quality.Windows import Ui_MainWindow, Modal_window_quit, Modal_window


class graphic_1(Reqests, Prep_records, QtWidgets.QWidget, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.Flag = True
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.groupBox.resize(790, 700)
        self.lineEdit.setText(os.getcwd())
        self.on_min.clicked.connect(self.showMinimized)
        self.quit.clicked.connect(self.close_program)
        self.pushButton.clicked.connect(self.report_and_map)
        self.pushButton_2.clicked.connect(self.report_only)
        self.pushButton_3.clicked.connect(self.only_map)


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()


    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def close_program(self):
        if threading.active_count() > 1:
            Modal_window_quit(self).exec_()
        else:
            self.close()


    def show_bar(self):
        self.groupBox.resize(790, 700)
        self.progressBar.show()
        self.label_8.show()
        self.label_8.setText(f"Готово 0/{len(self.cameras)}")


    def hide_bar(self):
        self.groupBox.resize(790, 570)
        self.label_8.hide()
        self.progressBar.hide()
        self.groupBox.resize(790, 570)


    def chek_data(self):
        if threading.active_count() > 1:
            Modal_window().exec_()
            return False
        self.textBrowser.setText("")
        if not os.path.isdir(self.lineEdit.text()):
            self.textBrowser.append("Некорректный путь")
            self.lineEdit.setStyleSheet("QLineEdit{border: 2px solid red}")
        else:
            self.lineEdit.setStyleSheet("QLineEdit{border: 2px solid black}")
            self.dir = f"{self.lineEdit.text()}"

        if self.tabWidget.currentIndex() == 0:
            if self.textEdit.toPlainText() == "":
                self.textBrowser.append("Введите хотя бы один id камеры")
                self.textEdit.setStyleSheet("QtextEdit{border: 3px solid red}")
            else:
                self.cameras = list(set(self.textEdit.toPlainText().split("\n")))
        else:
            if not os.path.exists(self.lineEdit_4.text()):
                self.textBrowser.append("Некорректный путь до файла с камерами")
                self.lineEdit_4.setStyleSheet("QLineEdit{border: 2px solid red;border-radius: 0px}")
            else:
                if not self.lineEdit_4.text().endswith(".txt"):
                    self.textBrowser.append("Некорректное разрешение файла, необходимо \".txt\"")
                    self.lineEdit_4.setStyleSheet("QLineEdit{border: 2px solid red;border-radius: 0px}")
                else:
                    with open(self.lineEdit_4.text(), "r") as file:
                        self.cameras = list(set(file.read().split("\n")))



        try:
            if not int(self.lineEdit_2.text()) in range(1, 31):
                self.textBrowser.append("Период должен быть от 1 до 30 дней")
                self.lineEdit_2.setStyleSheet("QLineEdit{border: 2px solid red}")
            else:
                self.days = int(self.lineEdit_2.text())
                self.lineEdit_2.setStyleSheet("QLineEdit{border: 2px solid black}")
        except:
            self.textBrowser.append("Введите число в поле периода")
            self.lineEdit_2.setStyleSheet("QLineEdit{border: 2px solid red}")

        try:
            if not int(self.lineEdit_3.text()) in range(100,10001):
                self.textBrowser.append("Количество результатов должно быть от 100 до 10000")
                self.lineEdit_3.setStyleSheet("QLineEdit{border: 2px solid red}")
            else:
                self.count_results = int(self.lineEdit_3.text())
                self.lineEdit_3.setStyleSheet("QLineEdit{border: 2px solid black}")
        except:
            self.textBrowser.append("Введите число в поле количчества данных")
            self.lineEdit_3.setStyleSheet("QLineEdit{border: 2px solid red}")

        if self.textBrowser.toPlainText() != "":
            return False
        else:
            self.textEdit.setText("")
            self.textBrowser.append("В работе...")
            return True


    def report_and_map(self):
        if self.chek_data():
            prep_repotr = threading.Thread(target=self.save_chart)
            prep_repotr.start()


    def only_map(self):
        if self.chek_data():
            prep_repotr = threading.Thread(target=self.save_map_only)
            prep_repotr.start()


    def report_only(self):
        if self.chek_data():
            prep_repotr = threading.Thread(target=self.save_report_only)
            prep_repotr.start()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = graphic_1()
    Dialog.show()
    sys.exit(app.exec_())

import base64
import ctypes
import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from Show_Main_Window import Show_Main
from Windows.Frame import FramelessWindow
from Windows.Icon import img_data

StyleSheet = """
/* Панель заголовка */
TitleBar {
    background-color: rgb(54, 100, 180);
    border-top: 5px solid black;
    border-left: 5px solid black;
    border-right: 5px solid black;
    border-top-left-radius:15px;
    border-top-right-radius:15px;

}

#Icon_label{
border-top-left-radius:15px;
background-color: black;}

/* Минимизировать кнопку `Максимальное выключение` Общий фон по умолчанию */
#buttonMinimum,#buttonMaximum,#buttonClose, #buttonMy {
    background-color: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
    border: 2px solid black;
    border-radius: 15px;
}
/* Зависание */
#buttonMinimum:hover,#buttonMaximum:hover {
    background-color: rgb(48, 141, 162);
}
#buttonClose:hover {
    color: white;
    background-color: rgb(232, 17, 35);
}


/* Мышь удерживать */
#buttonMinimum:pressed,#buttonMaximum:pressed {
    background-color: rgb(44, 125, 144);
}
#buttonClose:pressed {
    color: white;
    background-color: rgb(161, 73, 92);
}
"""



if __name__ == '__main__':
    myappid = u'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    with open("imageToSave.png", "wb") as Logo:
        Logo.write(base64.decodebytes(img_data))
        app_icon = QIcon("imageToSave.png")
    os.remove("imageToSave.png")
    w = FramelessWindow()
    w.setWindowTitle('Проверка качества детектов')
    w.setWindowIcon(app_icon)
    w.setWidget(Show_Main(w))
    w.show()
    sys.exit(app.exec_())
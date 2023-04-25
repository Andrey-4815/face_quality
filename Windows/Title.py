from PyQt5.QtCore import Qt, pyqtSignal, QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QPushButton)


class TitleBar(QWidget):
    windowMinimumed = pyqtSignal()
    windowMaximumed = pyqtSignal()
    windowNormaled = pyqtSignal()
    windowClosed = pyqtSignal()
    windowMoved = pyqtSignal(QPoint)


    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.mPos = None
        self.iconSize = 40

        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 5, 10, 0)


        self.iconLabel = QLabel(self)
        self.iconLabel.setContentsMargins(3, 0, 0, 0)
        layout.addWidget(self.iconLabel)

        self.titleLabel = QLabel(self)
        self.titleLabel.setMargin(2)
        layout.addWidget(self.titleLabel)

        font = self.font() or QFont()
        font.setFamily('Webdings')

        self.buttonMinimum = QPushButton('0', self, clicked=self.windowMinimumed.emit, font=font,objectName='buttonMinimum')
        layout.addWidget(self.buttonMinimum)

        self.buttonMaximum = QPushButton('1', self, clicked=self.showMaximized, font=font, objectName='buttonMaximum')
        layout.addWidget(self.buttonMaximum)

        self.buttonClose = QPushButton('r', self, clicked=self.windowClosed.emit, font=font, objectName='buttonClose')
        layout.addWidget(self.buttonClose)

        self.setHeight()


    def showMaximized(self):
        if self.buttonMaximum.text() == '1':
            self.buttonMaximum.setText('2')
            self.windowMaximumed.emit()
        else:
            self.buttonMaximum.setText('1')
            self.windowNormaled.emit()


    def setHeight(self, height=30):
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)
        self.buttonMinimum.setMaximumSize(height, height)
        self.buttonMaximum.setMaximumSize(height, height)
        self.buttonClose.setMaximumSize(height, height)


    def setTitle(self, title):
        self.titleLabel.setText(title)


    def setIcon(self, icon):
        self.iconLabel.setMaximumSize(44, 44)
        self.iconLabel.setPixmap(icon.pixmap(self.iconSize, self.iconSize))
        self.iconLabel.setObjectName("Icon_label")


    def setIconSize(self, size):
        self.iconSize = size


    def enterEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super(TitleBar, self).enterEvent(event)


    def mouseDoubleClickEvent(self, event):
        global flag
        super(TitleBar, self).mouseDoubleClickEvent(event)
        self.showMaximized()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()


    def mouseReleaseEvent(self, event):
        self.mPos = None
        event.accept()


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.windowMoved.emit(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()

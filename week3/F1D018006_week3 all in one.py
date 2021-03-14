import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MainWin(QWidget):

    def __init__(self):
        super().__init__()
        self.__red = 0
        self.__green = 0
        self.__blue = 0
        self.__boxSize = 20
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(400, 500)
        self.setWindowTitle('CHANGE MY STYLE')
        mainLayout = QVBoxLayout()
        layoutForm = QFormLayout()

        labelColor = QLabel("Colors :")
        labelRed = QLabel("Red")
        labelGreen = QLabel("Green")
        labelBlue = QLabel("Blue")
        labelSize = QLabel("Size")
        labelResult = QLabel("Drag this object")
        labelExit = QLabel("ESC to close",self)
        labelExit.move(0,475)

        self._lineRed = QLineEdit(str(self.__red))
        self._lineGreen = QLineEdit(str(self.__green))
        self._lineBlue = QLineEdit(str(self.__blue))

        setColorBtn = QPushButton('Apply color', self)
        setColorBtn.clicked.connect(lambda:self.changeColor())

        # slider
        self._setSize = QSlider(Qt.Horizontal)
        self._setSize.valueChanged.connect(lambda:self.changeSize())

        self._colorObj = DragButton(self)
        self._colorObj.move(self.rect().center())
        self._colorObj.setFixedSize(self.__boxSize,self.__boxSize)

        layoutForm.addRow(labelColor,None)
        layoutForm.addRow(labelRed,self._lineRed)
        layoutForm.addRow(labelGreen,self._lineGreen)
        layoutForm.addRow(labelBlue,self._lineBlue)
        layoutForm.addRow(None, setColorBtn)
        layoutForm.addRow(labelSize,self._setSize)
        layoutForm.addRow(labelResult,None)

        self.changeColor()

        mainLayout.addLayout(layoutForm)

        self.setLayout(mainLayout)
        self.show()

    def changeColor(self):
        self.__red = int (self._lineRed.text())
        self.__green = int (self._lineGreen.text())
        self.__blue = int (self._lineBlue.text())
        style = f"background-color:rgb({self.__red},{self.__green},{self.__blue});" \
                f"color:rgb({255-self.__red},{255-self.__green},{255-self.__blue});" \
                f"border:1px solid black;"
        self._colorObj.setStyleSheet(style)

    def changeSize(self):
        a = self._setSize.value()*2+20
        self._colorObj.setFixedSize(a,a)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

class DragButton(QPushButton):

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)
            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)

def main():
    app = QApplication(sys.argv)
    ex = MainWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

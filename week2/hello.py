import sys
from PyQt5.QtWidgets import *


def window():
    app = QApplication(sys.argv)

    w = QWidget()
    b = QLabel(w)

    w.setGeometry(500, 500, 400, 400)
    w.setWindowTitle('PyQt5')

    b.setText('Hello World')
    b.move(50, 20)
    b.setToolTip('Hello Tooltips')

    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

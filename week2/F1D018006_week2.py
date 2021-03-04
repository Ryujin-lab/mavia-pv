#NAMA : ALIDIN
#NIM  : F1D018006
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindows:
  def __init__(self):
    app = QApplication(sys.argv)

    frame = QWidget()
    frame.setFixedSize(500,250)
    frame.setWindowTitle("Hello World PYQT")

    myfont = QFont('Arial',15)

    label = QLabel(frame)
    label.setGeometry(0,0,500,50)
    label.setText("MINGGU 1 : HELLO WORLD APP")
    label.setAlignment(Qt.AlignCenter)
    label.setFont(QFont('Arial',15 , QFont.Bold))
    
    labelName = QLabel(frame)
    labelName.setGeometry(50,60,100,50)
    labelName.setText("NAMA : ")
    labelName.setAlignment(Qt.AlignCenter)
    labelName.setFont(QFont('Arial',15 , QFont.Bold))

    self.textfield = QLineEdit(frame)
    self.textfield.setGeometry(150,60,300,50)
    self.textfield.setFont(myfont)

    self.button = QPushButton(frame)
    self.button.setGeometry(50,120,400,50)
    self.button.setText("SUBMIT")
    self.button.setFont(myfont)

    self.res = QLabel(frame)
    self.res.setGeometry(50,180,400,50)
    self.res.setText("HELLO, WORLD!")
    self.res.setAlignment(Qt.AlignCenter)
    self.res.setFont(QFont('Arial',15))

    self.button.clicked.connect(lambda:self.buttonClicked())
    frame.show()
    sys.exit(app.exec_())

  def buttonClicked(self):
    text = self.textfield.text()
    self.res.setText("HELLO, "+text.upper()+"!")

def main():
  app = MainWindows()

if __name__ == "__main__":
  main()
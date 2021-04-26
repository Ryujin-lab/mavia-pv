import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Input Dialog")
		
    layout = QFormLayout()

    self.btn_lang = QPushButton("Choose from list")
    self.btn_lang.clicked.connect(self.getItem)
		
    self.le = QLineEdit()
    self.btn_name = QPushButton("get name")
    self.btn_name.clicked.connect(self.gettext)
		
    self.le1 = QLineEdit()
    self.btn_integer = QPushButton("Enter an integer")
    self.btn_integer.clicked.connect(self.getint)
		
    self.le2 = QLineEdit()
    
    self.setLayout(layout)
    layout.addRow(self.btn_lang,self.le)
    layout.addRow(self.btn_name,self.le1)
    layout.addRow(self.btn_integer,self.le2)
		
  def getItem(self):
    langs = ("C", "C++", "Java", "Python")
    lang, ok = QInputDialog.getItem(self, "select input dialog", 
      "list of languages", langs, 0, False)

    if ok and lang:
      self.le.setText(lang)
			
  def gettext(self):
    text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')

    if ok:
      self.le1.setText(str(text))
			
  def getint(self):
    num,ok = QInputDialog.getInt(self,"integer input dualog","enter a number")

    if ok:
      self.le2.setText(str(num))
			
def main(): 
  app = QApplication(sys.argv)
  apply_stylesheet(app, theme='dark_teal.xml')
  ex = MainWin()
  ex.show()
  sys.exit(app.exec_())
	
if __name__ == '__main__':
  main()
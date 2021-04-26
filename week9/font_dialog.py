import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class MainWin(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("Font Dialog")
      self.setFixedSize(200,200)
		
      layout = QVBoxLayout()
      self.setLayout(layout)

      self.btn_font = QPushButton("choose font")
      self.btn_font.clicked.connect(self.getfont)

      self.label = QLabel("Hello World")
      self.label.setStyleSheet(("font-size:20px"))

      layout.addWidget(self.btn_font)
      layout.addWidget(self.label)
		
   def getfont(self):
      font, ok = QFontDialog.getFont()
		
      if ok:
         self.label.setFont(font)
			
def main():
   app = QApplication(sys.argv)
   ex = MainWin()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
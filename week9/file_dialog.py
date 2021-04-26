import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("File Dialogue")
    layout = QVBoxLayout()
    self.setLayout(layout)

    self.btn_open_file = QPushButton("Open File")
    self.btn_open_file.clicked.connect(self.getfile)
		
    self.btn_open_files = QPushButton("QFileDialog object")
    self.btn_open_files.clicked.connect(self.getfiles)
		
    self.contents = QTextEdit()
    self.image = QLabel()

    layout.addWidget(self.btn_open_file)
    layout.addWidget(self.btn_open_files)
    layout.addWidget(self.image)
    layout.addWidget(self.contents)
		
  def getfile(self):
    fname,_ = QFileDialog.getOpenFileName(self, 'Open file', 
      'c:\\',"Image files (*.jpg *.gif *.png)")
    self.image.setPixmap(QPixmap(fname))
		
  def getfiles(self):
    dlg = QFileDialog()
    dlg.setFileMode(QFileDialog.AnyFile)

    dlg.setNameFilter("Text files (*.txt)")
    filenames = list()
		
    if dlg.exec_():
      filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')
			
      with f:
        data = f.read()
        self.contents.setText(data)
				
def main():
  app = QApplication(sys.argv)
  apply_stylesheet(app, theme='dark_teal.xml')
  ex = MainWin()
  ex.show()
  sys.exit(app.exec_())
	
if __name__ == '__main__':
  main()
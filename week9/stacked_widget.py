import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(300,150)

    self.leftlist = QListWidget ()
    self.leftlist.insertItem (0, 'Contact' )
    self.leftlist.insertItem (1, 'Personal' )
    self.leftlist.insertItem (2, 'Educational' )
		
    self.contact_stack = QWidget()
    self.personal_stack = QWidget()
    self.edu_stack = QWidget()
		
    self.contact_stackUI()
    self.personal_stackUI()
    self.edu_stackUI()
		
    self.Stack = QStackedWidget (self)
    self.Stack.addWidget (self.contact_stack)
    self.Stack.addWidget (self.personal_stack)
    self.Stack.addWidget (self.edu_stack)
		
    hbox = QHBoxLayout(self)
    hbox.addWidget(self.leftlist)
    hbox.addWidget(self.Stack)

    self.setLayout(hbox)
    self.leftlist.currentRowChanged.connect(self.display)
    self.setWindowTitle('StackedWidget demo')
    self.show()
		
  def contact_stackUI(self):
    layout = QFormLayout()
    layout.addRow("Name",QLineEdit())
    layout.addRow("Address",QLineEdit())
    #self.setTabText(0,"Contact Details")
    self.contact_stack.setLayout(layout)
		
  def personal_stackUI(self):
    layout = QFormLayout()
    sex = QHBoxLayout()
    sex.addWidget(QRadioButton("Male"))
    sex.addWidget(QRadioButton("Female"))
    layout.addRow(QLabel("Sex"),sex)
    layout.addRow("Date of Birth",QLineEdit())
		
    self.personal_stack.setLayout(layout)
		
  def edu_stackUI(self):
    layout = QHBoxLayout()
    layout.addWidget(QLabel("subjects"))
    layout.addWidget(QCheckBox("Physics"))
    layout.addWidget(QCheckBox("Maths"))
    self.edu_stack.setLayout(layout)
		
  def display(self,i):
    self.Stack.setCurrentIndex(i)
		
def main():
  app = QApplication(sys.argv)
  ex = MainWin()
  sys.exit(app.exec_())
	
if __name__ == '__main__':
  main()
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qt_material import apply_stylesheet

class MainWin(QTabWidget):
   def __init__(self):
      super().__init__()
      self.setFixedSize(400,200)
      self.contact_tab = QWidget()
      self.personal_tab = QWidget()
      self.education_tab = QWidget()
		
      self.addTab(self.contact_tab,"Tab 1")
      self.addTab(self.personal_tab,"Tab 2")
      self.addTab(self.education_tab,"Tab 3")
      self.contact_detail_tab()
      self.personal_detail_tab()
      self.education_detail_tab()
      self.setWindowTitle("tab demo")
		
   def contact_detail_tab(self):
      layout = QFormLayout()
      layout.addRow("Name",QLineEdit())
      layout.addRow("Address",QLineEdit())
      self.setTabText(0,"Contact Details")
      self.contact_tab.setLayout(layout)
		
   def personal_detail_tab(self):
      layout = QFormLayout()
      sex = QHBoxLayout()
      sex.addWidget(QRadioButton("Male"))
      sex.addWidget(QRadioButton("Female"))
      layout.addRow(QLabel("Sex"),sex)
      layout.addRow("Date of Birth",QLineEdit())
      self.setTabText(1,"Personal Details")
      self.personal_tab.setLayout(layout)
		
   def education_detail_tab(self):
      layout = QHBoxLayout()
      layout.addWidget(QLabel("subjects")) 
      layout.addWidget(QCheckBox("Physics"))
      layout.addWidget(QCheckBox("Maths"))
      self.setTabText(2,"Education Details")
      self.education_tab.setLayout(layout)
		
def main():
   app = QApplication(sys.argv)
   ex = MainWin()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from qt_material import apply_stylesheet

class MainWin(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self._init_ui()
        self.show()

    def _init_ui(self):
        self.setFixedSize(500,300)
        self._init_menu_bar()
        # create menu


    def _init_menu_bar(self):
        menubar = QMenuBar()
        self.layout.addWidget(menubar, 0, 0)
        actionFile = menubar.addMenu("File")
        New = QAction(QIcon("add.svg"), "New", self)
        Open = QAction(QIcon("folder.svg"),"Open", self)
        Save = QAction(QIcon("save.svg"),"Save", self)
        Quit = QAction("Quit", self)

        Open.triggered.connect(lambda :self.getfile())
        Quit.triggered.connect(lambda :self.quit())

        actionFile.addAction(New)
        actionFile.addAction(Open)
        actionFile.addAction(Save)
        actionFile.addSeparator()
        actionFile.addAction(Quit)

        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")

        tbox = QPlainTextEdit()
        self.layout.addWidget(tbox, 1, 0)

    # def _init_toolbar(self):

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif)")

    def quit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("Keluar Aplikasi?")
        msg.setInformativeText("apakah anda yakin akan keluar? \nseluruh perubahan akan terhapus!")
        msg.setWindowTitle("keluar aplikasi")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        retval = msg.exec_()

        if(retval == msg.Yes ):
            QApplication.quit()

def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    ex = MainWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

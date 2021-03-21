import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__();
        self.data = {"judul": [],
                     "deskripsi": [],
                     "tanggal": [],
                     "waktu": []}
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setFixedSize(400, 600)
        self.setWindowTitle("Simple Todo List App")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.header())
        main_layout.addLayout(self.form())
        self.tabel = self.result()
        main_layout.addWidget(self.tabel)
        main_layout.addStretch(10)
        self.setLayout(main_layout)

    def header(self):
        title = QLabel("SIMPLE TODO LIST APP")
        title.setFixedSize(400, 30)
        return title

    def form(self):
        form = QFormLayout()
        task_title = QLabel("Judul")
        task_description = QLabel("Deskripsi")
        task_date = QLabel("Tanggal")
        task_time = QLabel("waktu")

        self.input_title = QLineEdit()
        self.input_description = QTextEdit()
        self.input_description.setFixedHeight(50)
        self.input_date = QLineEdit()
        self.input_time = QLineEdit()

        sub_layout = QHBoxLayout()
        btn_cancel = QPushButton("Cancel")
        btn_submit = QPushButton("Submit")
        btn_submit.clicked.connect(lambda :self.submit())
        btn_cancel.clicked.connect(lambda :self.cancel())

        sub_layout.addWidget(btn_cancel)
        sub_layout.addWidget(btn_submit)

        form.addRow(task_title, self.input_title)
        form.addRow(task_description, self.input_description)
        form.addRow(task_date, self.input_date)
        form.addRow(task_time, self.input_time)
        form.addRow(None, sub_layout)

        return form

    def result(self):
        table = TableView(self.data, 0, 4)
        return table

    def cancel(self):
        self.input_title.setText("")
        self.input_description.clear()
        self.input_date.setText("")
        self.input_time.setText("")

    def submit(self):
        data = []
        data.append(self.input_title.text())
        data.append(self.input_description.toPlainText() )
        data.append(self.input_date.text())
        data.append(self.input_time.text())
        self.tabel.addData(data)


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []

        for n, key in enumerate(self.data.keys()):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

    def addData(self, row_data):
        row = self.rowCount()
        self.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            self.setItem(row, col, cell)
            col += 1


def main():
    app = QApplication(sys.argv)
    ex = MainWin()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

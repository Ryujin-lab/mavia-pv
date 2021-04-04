import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

'''
Tugas:
1. Munculkan `_nim` pada label
2. Sesuaikan variabel `_nim` sesuai dengan NIM masing-masing
3. Hubungkan signal `valueChanged()` pada `sp` dengan method `_on_change()`
4. Gunakan angka yang ada pada `_nim` mulai karakter ke-4, contohnya F1B008004 = '008004' untuk mencari beberapa nilai berikut:
   a. Angka terkecil gunakan sebagai `setMinimum()`
   b. Angka terbesar gunakan sebagai `setMaximum()`
'''
_nim = 'F1D018006'
class SpinBox(QWidget):
    def __init__(self, parent=None):
        super(SpinBox, self).__init__(parent)

        __nim = list(_nim)[3:]

        nilai_maximal = int(max(__nim))
        nilai_minimal = int(min(__nim))
        ___max = nilai_maximal
        ___min = nilai_minimal

        layout = QVBoxLayout()
        self.l1 = QLabel('Nilai: 0')
        self.l1.setAlignment(Qt.AlignRight)
        layout.addWidget(self.l1)

        self.sp = QSpinBox()
        self.sp.setMinimum(___min)
        self.sp.setMaximum(___max)
        self.sp.valueChanged.connect(self._on_change)
        layout.addWidget(self.sp)

        self.setLayout(layout)
        self.setWindowTitle("SpinBox")

    def _on_change(self):
        self.l1.setText('Nilai: ' + str(self.sp.value()))


def main():
    app = QApplication(sys.argv)
    sb = SpinBox()
    sb.setGeometry(100, 100, 300, 200)
    sb.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
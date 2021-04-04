import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''
Tugas:
1. Munculkan `_nim` pada label
2. Sesuaikan variabel `_nim` sesuai dengan NIM masing-masing
3. Hubungkan signal `valueChanged()` pada `sl` dengan method `_on_change()`
4. Gunakan angka yang ada pada `_nim` mulai karakter ke-4, contohnya F1B008004 = '008004' untuk mencari beberapa nilai berikut:
   a. Angka terkecil gunakan sebagai `setMinimum()`
   b. Angka terbesar gunakan sebagai `setMaximum()`
   c. Cari nilai tengah antara `___min` dan `___max` dan gunakan sebagai `setValue()`
'''

_nim = 'F1D018006'
class Slider(QWidget):

    def __init__(self, parent=None):
        super(Slider, self).__init__(parent)

        __nim = list(_nim)[3:]

        nilai_max = int(max(__nim))
        nilai_min = int(min(__nim))

        ___min = nilai_min * 10 + 1
        ___max = nilai_max * 10 + 1
        ___med = int((___max - ___min) / 2)

        layout = QVBoxLayout()
        self.l1 = QLabel(_nim)
        self.l1.setAlignment(Qt.AlignCenter)
        self.l1.setFont(QFont('Century', ___med))
        layout.addWidget(self.l1)

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(___min)
        self.sl.setMaximum(___max)
        self.sl.setValue(___med)
        self.sl.setTickPosition(QSlider.TicksAbove)
        self.sl.setTickInterval(10)

        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self._on_change)
        self.setLayout(layout)
        self.setWindowTitle("Slider")

    def _on_change(self):
        self.l1.setFont(QFont('Century', self.sl.value()))


def main():
    app = QApplication(sys.argv)
    sl = Slider()
    sl.setGeometry(100, 100, 500, 200)
    sl.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
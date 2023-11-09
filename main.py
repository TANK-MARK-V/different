import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainW


class Yellow(QMainWindow, Ui_MainW):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def do(self, qp):
        xl, yl, diam = random.choice(range(100, 650)), random.choice(
            range(100, 450)), random.choice(range(10, 130))

        qp.setBrush(QColor(random.choice(range(0, 255)), random.choice(range(0, 255)),
                           random.choice(range(0, 255))))
        qp.drawEllipse(xl, yl, diam, diam)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.do(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow()
    ex.show()
    sys.exit(app.exec_())

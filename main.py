import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from PyQt5 import uic

class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.circle = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.x, self.y = random.randint(50, 300), random.randint(50, 250)
        self.diameter = random.randint(10, 120)
        self.circle = True

    def paintEvent(self, event):
        if self.circle:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp):
        pen = QPen(Qt.yellow, 2)
        qp.setPen(pen)
        qp.drawEllipse(self.x, self.y, self.diameter, self.diameter)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())

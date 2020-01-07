import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from UI import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circle = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.x, self.y = random.randint(50, 300), random.randint(50, 250)
        self.diameter = random.randint(10, 120)
        self.pen = QPen(QColor(random.randint(0, 255), random.randint(0, 255),
                               random.randint(0, 255)), 2)

        self.circle = True

    def paintEvent(self, event):
        if self.circle:
            qp = QPainter()
            qp.begin(self)
            self.drawCircle(qp)
            qp.end()

    def drawCircle(self, qp):
        qp.setPen(self.pen)
        qp.drawEllipse(self.x, self.y, self.diameter, self.diameter)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())

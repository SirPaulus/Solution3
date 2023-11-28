import io
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createCircle = QtWidgets.QPushButton(self.centralwidget)
        self.createCircle.setGeometry(QtCore.QRect(264, 312, 221, 81))
        self.createCircle.setObjectName("createCircle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.createCircle.clicked.connect(self.circle)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createCircle.setText(_translate("MainWindow", "Создать Круг"))


class Test(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.colors = [QColor(0, 255, 0), QColor(255, 0, 0), QColor(255, 255, 0), QColor(0, 255, 255)]
        self.draw = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)

    def run(self, qp):
        if self.draw:
            x = random.randint(10, 150)
            y = random.randint(10, 150)
            w = random.randint(10, 100)
            h = random.randint(10, 100)
            self.color = random.choice(self.colors)
            qp.setPen(self.color)
            qp.drawEllipse(x, y, w, h)
            self.draw = False
            qp.end()

    def circle(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())

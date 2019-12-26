from PyQt5 import QtWidgets, QtCore, QtGui, uic
from random import randint


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        uic.loadUi("UI.ui", self)

        self.pushButton.clicked.connect(self.update)
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.yellow))
        size = randint(50, 400)
        x = randint(10, self.frameGeometry().width() - size)
        y = randint(10, self.frameGeometry().height() - size)
        painter.drawEllipse(x, y, size, size)


if __name__ == "__main__":
    app = QtWidgets.QApplication([""])
    main = Main()
    main.show()
    app.exec()
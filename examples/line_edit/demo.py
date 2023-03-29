# coding:utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from qfluentwidgets import LineEdit, PushButton


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.lineEdit = LineEdit('', self)
        self.button = PushButton('按钮', self)
        self.resize(500, 500)
        self.lineEdit.move(110, 220)
        self.button.move(320, 220)
        self.lineEdit.resize(200, 33)
        self.lineEdit.setClearButtonEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec()
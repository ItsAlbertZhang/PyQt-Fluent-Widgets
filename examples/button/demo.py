# coding:utf-8
import sys

from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QAction
from qfluentwidgets import (DropDownPushButton, DropDownToolButton, PushButton, PrimaryPushButton,
                            HyperlinkButton, setTheme, Theme, ToolButton, ToggleButton, RoundMenu)
from qfluentwidgets import FluentIcon as FIF


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        # setTheme(Theme.DARK)

        self.toolButton = ToolButton(FIF.SETTING, self)

        # change the size of tool button
        # self.toolButton.resize(50, 50)
        # self.toolButton.setIconSize(QSize(30, 30))

        self.pushButton1 = PushButton('Standard push button')
        self.pushButton2 = PushButton('Standard push button with icon', self, FIF.FOLDER)

        self.primaryButton1 = PrimaryPushButton('Accent style button', self)
        self.primaryButton2 = PrimaryPushButton('Accent style button with icon', self, FIF.UPDATE)

        self.toggleButton = ToggleButton('Toggle Button', self, FIF.SEND)

        self.dropDownPushButton = DropDownPushButton('Email', self, FIF.MAIL)
        self.dropDownToolButton = DropDownToolButton(FIF.MAIL, self)
        self.menu = RoundMenu(parent=self)
        self.menu.addAction(QAction(FIF.SEND_FILL.icon(), 'Send'))
        self.menu.addAction(QAction(FIF.SAVE.icon(), 'Save'))
        self.dropDownPushButton.setMenu(self.menu)
        self.dropDownToolButton.setMenu(self.menu)

        self.hyperlinkButton = HyperlinkButton(
            url='https://github.com/zhiyiYo/PyQt-Fluent-Widgets',
            text='Hyper link button',
            parent=self
        )

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.toolButton, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.pushButton1, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.pushButton2, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.primaryButton1, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.primaryButton2, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.toggleButton, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.dropDownPushButton, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.dropDownToolButton, 0, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.hyperlinkButton, 0, Qt.AlignCenter)
        self.vBoxLayout.setSizeConstraint(QVBoxLayout.SetMinAndMaxSize)

        self.resize(500, 600)
        self.setStyleSheet('Demo{background:white}')



if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()
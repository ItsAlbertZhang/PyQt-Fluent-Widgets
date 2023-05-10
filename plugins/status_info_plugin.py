# coding: utf-8
from PySide6.QtCore import Qt
from PySide6.QtDesigner import QDesignerCustomWidgetInterface

from qfluentwidgets import InfoBar, ProgressBar, IndeterminateProgressBar, ProgressRing, StateToolTip, InfoBarPosition

from plugin_base import PluginBase


class StatusInfoPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Status & Info)'


class InfoBarPlugin(StatusInfoPlugin, QDesignerCustomWidgetInterface):
    """ Info bar plugin """

    def createWidget(self, parent):
        return InfoBar.success(
            title='Lesson 5',
            content='最短的捷径就是绕远路，绕远路才是我的最短捷径。',
            duration=-1,
            position=InfoBarPosition.NONE,
            parent=parent
        )

    def icon(self):
        return super().icon("InfoBar")

    def name(self):
        return "InfoBar"


class ProgressBarPlugin(StatusInfoPlugin, QDesignerCustomWidgetInterface):
    """ Progress bar plugin """

    def createWidget(self, parent):
        return ProgressBar(parent)

    def icon(self):
        return super().icon("ProgressBar")

    def name(self):
        return "ProgressBar"


class IndeterminateProgressBarPlugin(StatusInfoPlugin, QDesignerCustomWidgetInterface):
    """ Indeterminate progress bar plugin """

    def createWidget(self, parent):
        return IndeterminateProgressBar(parent)

    def icon(self):
        return super().icon("ProgressBar")

    def name(self):
        return "IndeterminateProgressBar"


class ProgressRingPlugin(StatusInfoPlugin, QDesignerCustomWidgetInterface):
    """ Progress ring plugin """

    def createWidget(self, parent):
        return ProgressRing(parent)

    def icon(self):
        return super().icon("ProgressRing")

    def name(self):
        return "ProgressRing"


class StateToolTipPlugin(StatusInfoPlugin, QDesignerCustomWidgetInterface):
    """ State tool tip plugin """

    def createWidget(self, parent):
        return StateToolTip('Running', 'Please wait patiently', parent)

    def icon(self):
        return super().icon("ProgressRing")

    def name(self):
        return "StateToolTip"

from PyQt5.QtWidgets import QRadioButton
from pyqt_ani_abstractbutton import AniAbstractButton


class AniRadioButton(QRadioButton, AniAbstractButton):
    def __init__(self):
        super().__init__()

    def _initStyle(self, border_width):
        self.setStyleSheet(self._getStyle(border_width) + 'QRadioButton::indicator { border: none; }')
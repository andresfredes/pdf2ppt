# Copyright 2021, Andres Fredes, <andres.hector.fredes@gmail.com>
# 
# This file is part of pdf2ppt.
# 
#     pdf2ppt is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     pdf2ppt is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with pdf2ppt.  If not, see <https://www.gnu.org/licenses/>.

"""custom_widgets.py: helper / wrapper classes for the QtWidgets used in the
program. Provides a neat way to keep the customising/styling out of the main UI
code.
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QPushButton, QLabel
from PyQt5.QtGui import QFont

class Action(QAction):
    """A menu option with associated function, keyboard shortcut and status tip.

    Args:
        name (str): menu option name.
        window (QMainWindow): the menu's parent window.
        shortcut (str): keyboard shortcut for the menu option.
        tip (str): status hint displayed on mouse hover event.
        func (function): function to be called when menu option is selected.
    """
    def __init__(self, name, window, shortcut, tip, func):
        super().__init__(name, window)
        self.setShortcut(shortcut)
        self.setStatusTip(tip)
        self.triggered.connect(func)


class Button(QPushButton):
    """A button widget with defined display text and function to activate when
    clicked.

    Args:
        text (str): text to be displayed within the button. Defaults to empty.
        func (function): function to be run when button is clicked. Defaults to
            None.
        active (boolean): determines whether button is active when instantiated.
    """
    def __init__(self, text="", func=None, active=True):
        super().__init__()
        self.setText(text)
        if func:
            self.clicked.connect(func)
        self.setFont(Font())
        self.setEnabled(active)

    def disable(self):
        """Quick means to disable the button while processing conversion
        """
        self.setEnabled(False)

    def enable(self):
        """Quick means to enable the button when safe
        """
        self.setEnabled(True)


class Label(QLabel):
    """A label widget with defined inner text, size and font style.

    Args:
        text (str): text to be displayed.
        size (int): font point size. Defaults to 20.
        style (str): font style ('strike', 'bold' or 'italic').
            Defaults to None.
    """
    def __init__(self, text="", size=20, style=None):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        font = Font(size, style)
        self.setFont(font)


class Font(QFont):
    """A font element to be included in labels and other widgets that display
    text.

    Args:
        size (int): font point size. Defaults to 20.
        style (str): font style ('strike', 'bold' or 'italic').
            Defaults to None.
    """
    def __init__(self, size=20, style=None):
        super().__init__()
        self.setPointSize(size)
        if style == "strike":
            self.setStrikeOut(True)
        if style == "italic:":
            self.setItalic(True)
        if style == "bold":
            self.setBold(True)
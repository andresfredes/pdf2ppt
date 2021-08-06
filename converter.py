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

"""coverter.py: Custom worker object to run conversion on secondary thread.
This avoids locking the gui during file processing.

The core logic is handled by the pdf2pptx library, which can be found at:
https://github.com/kevinmcguinness/pdf2pptx

It, in turn uses PyMuPDF and python-pptx which can be found at:
https://github.com/pymupdf/PyMuPDF
and
https://github.com/scanny/python-pptx
"""

from PyQt5.QtCore import QObject, pyqtSignal
import pdf2pptx as p2p

class Converter(QObject):
    """Simple worker function to handle file conversion in a secondary thread
    to avoid locking the GUI.

    Thread management is done by the GUI itself, but this is the object that
    will be passed to the secondary thread to manage the comparatively slower
    task of converting the files.

    Class variables:
        finished (pyqtSignal): Signal emitted to main thread when task complete.
        warning (pyqtSignal): Signal emitted to main thread when task failed.

    Args:
        path (str): path of file to convert
    """
    finished = pyqtSignal()
    warning = pyqtSignal()

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        """Converts the selected file.

        This function is triggered when the object is moved onto the secondary
        thread. It emits a finished signal on success and warning on failure.
        """
        try:
            p2p.main(self.path)
        except Exception as e:
            print(e)
            self.warning.emit()
        else:
            self.finished.emit()
        
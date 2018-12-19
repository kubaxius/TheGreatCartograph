# TheGreatCartograph - creating maps like professional.
# Copyright (C) 2018  Jakub Niedźwiedź
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Contact me at jakub.niedzwiedz98@gmail.com,
# or via LinkedIn: https://www.linkedin.com/in/kuba-nied%C5%BAwied%C5%BA-2a1a3115b/
# 
# MainWindow.py
# TODO: FILE DESCRIPTION
# 

from PyQt5 import QtWidgets
from view.layout.mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    # TODO: MainWindow - file is a template

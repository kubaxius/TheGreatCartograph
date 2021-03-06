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
# __init__.py
# TODO: FILE DESCRIPTION
#
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

# from model.AdministrativeUnit import AdministrativeUnit
from model.setup import global_init
from menu.MainWindow import MainWindow
from menu.ToolPalette import ToolPaletteDocker


def main():
    global_init('test')

    # p = AdministrativeUnit()
    # p.name = "Test"
    # p.save()

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("TheGreatCartograph")
    w.show()
    t = ToolPaletteDocker()
    w.addDockWidget(Qt.LeftDockWidgetArea, t)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()



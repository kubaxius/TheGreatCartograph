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
# tool.py
# Module consisting of all cursor tools and of their enumeration.
#
import resources.icons
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QAction, QActionGroup


class Tool(QAction):

    def __init__(self, group: QActionGroup):
        super().__init__()
        self.setCheckable(True)
        self.triggered.connect(self.on_trigger_of_button)
        self.setActionGroup(group)

    def set_icon(self, icon_path, icon_text):
        self.setIcon(QIcon(QPixmap(icon_path)))
        self.setIconText(icon_text)

    def on_trigger_of_button(self):
        pass

    def on_mouse_click(self):
        pass


class BorderPen(Tool):
    pass


class BorderMove(Tool):
    pass

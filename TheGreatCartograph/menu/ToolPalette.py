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
# ToolPalette.py
# TODO: FILE DESCRIPTION
#
import json

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import data.tool as tool
import inspect


class ToolPalette(QtWidgets.QToolBar):
    """Controller for ToolPalette of TGC.
    """

    def __init__(self):
        super().__init__()
        self.actions_instances = []
        self.action_group = QtWidgets.QActionGroup(self)
        self.setOrientation(Qt.Vertical)
        self.add_tools()
        self.style_tools()

    def add_tools(self):
        # iterate over every class in data.tool file in reversed order
        for name, action in reversed(inspect.getmembers(tool)):

            # check if is an child of Tool, but not the Tool itself
            if inspect.isclass(action) and issubclass(action, tool.Tool) and name != tool.Tool.__name__:
                a = action(self.action_group)
                self.addAction(a)
                # necessary to prevent garbage collector from killing action
                self.actions_instances.append(a)

    def style_tools(self):
        with open("view/tool_values.json", "r") as read_file:
            tool_values = json.load(read_file)
            for action in self.actions():
                if issubclass(type(action), tool.Tool):
                    for method_name in tool_values[type(action).__name__]:
                        attributes = tool_values[type(action).__name__][method_name]
                        method = getattr(action, method_name)
                        if type(attributes) == list:
                            method(*attributes)
                        else:
                            method(attributes)


class ToolPaletteDocker(QtWidgets.QDockWidget):
    def __init__(self):
        super().__init__()
        self.setWidget(ToolPalette())

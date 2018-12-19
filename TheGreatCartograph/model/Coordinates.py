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
# Coordinates.py
# Class that is used to store coordinates on globe.
# 
import mongoengine


class Coordinates(mongoengine.EmbeddedDocument):
    longitude = 0  # angle from prime meridian, with vertex at pole, 0° - 360°
    latitude = 0  # parallel to the equator, 0° - 180°

    def __init__(self, latitude, longitude):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude

    @property
    def x(self):
        return self.longitude

    @x.setter
    def x(self, x):
        self.longitude = x

    @property
    def y(self):
        return self.latitude

    @y.setter
    def y(self, y):
        self.latitude = y

    meta = {
        'db_alias': 'core',
        'collection': 'world',
        'indexes': [
            'created',
            'name'
        ],
        'ordering': ['name']
    }

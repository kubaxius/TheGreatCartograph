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
# AdministrativeUnit.py
# TODO: FILE DESCRIPTION
# 
import datetime
import mongoengine as mongoengine
from model.Coordinates import Coordinates


class AdministrativeUnit(mongoengine.EmbeddedDocument):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    administrative_units = mongoengine.ListField(mongoengine.ObjectIdField())
    borders = mongoengine.ListField(mongoengine.ObjectIdField())
    coordinates = Coordinates(0, 0)

    def __init__(self, x: float, y: float):
        super().__init__()
        self.coordinates = Coordinates(x, y)

    meta = {
        'db_alias': 'core',
        'collection': 'administrative-units',
        'indexes': [
            'created',
            'name'
        ],
        'ordering': ['name']
    }
    # TODO: AdministrativeUnit - file is a template

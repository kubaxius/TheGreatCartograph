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
# World.py
# TODO: FILE DESCRIPTION
# 
import datetime
import mongoengine as mongoengine


class World(mongoengine.Document):
    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'world',
        'indexes': [
            'created',
            'name'
        ],
        'ordering': ['name']
    }
    # TODO: World - file is a template

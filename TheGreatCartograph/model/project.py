# project.py
# This file is responsible for handling all saving and loading to and from user's project.


class Project:

    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, '+w')
        pass

#!/usr/bin/python3
"""Module for the FileStorage class of airbnb clone"""
import json
import datetime
import os


class FileStorage:
    """Defines a class for storing and retrieving data"""


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function that returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Function to set in __object with key <obj.__class__.__name__, obj.id>"""
        if obj:
            key = '{}.{}'.format(type(obj).__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Function to save/serialize object to json file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """Function to reload saved objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                new_obj = json.load(f)
                FileStorage.__objects = new_obj
        except FileNotFoundError:
            pass

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
        return self.__objects

    def new(self):
        """Function to set in __object with key <obj.__class__.__name__, obj.id>"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Function to save/serialize object to json file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dic = {key: value.to_dict() for key, value in self.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        """Function to reload saved objects"""
        with open(self.__file_path, "r", encoding="utf-8") as f:
            new_obj_dict = json.load(f)
        for key, value in new_obj_dict.items():
            obj = self.classes()[value["__class__"]](**value)
            self.__objects[key] = obj

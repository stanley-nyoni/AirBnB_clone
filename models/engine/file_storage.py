#!/usr/bin/python3
"""Module for the FileStorage class of airbnb clone"""
import json
import datetime
import os
from models.base_model import BaseModel


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
        """Serializes __objects to JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            serialized_objects = {k: val.to_dict() for k, val, in FileStorage.__objects.items()}
            json.dump(serialized_objects, file)

    def base_class(self):
        """rreturns the dictionary of the base class and it's value"""
        classes = {"BaseModel": BaseModel}
        return classes

    def attributes(self):
        """Returns the valid attribute and its types"""
        attributes = {
            "BaseModel": {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime}
        }
        return attributes

    def reload(self):
        """Function to reload saved objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = obj_dict = {k: self.base_class()[val["__class__"]](**val)
                        for k, val in obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

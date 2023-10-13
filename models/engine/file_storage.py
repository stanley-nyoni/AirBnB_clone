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
        """Sets in __object with key <obj.__class__.__name__, obj.id>"""
        if obj:
            key = '{}.{}'.format(type(obj).__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            ser_obj = {k: val.to_dict()
                       for k, val, in FileStorage.__objects.items()}
            json.dump(ser_obj, file)

    def all_classes(self):
        """Returns the dictionary of the base class and it's value"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attribute and its types"""
        attributes = {
                "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                "State":
                {"name": str},
                "City":
                {"state": str,
                    "name": str},
                "Amenity":
                {"name": str},
                "Place":
                {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_per_night": int,
                    "latitude": float,
                    "longitute": float,
                    "amenity_ids": list},
                "Review":
                {"place_id": str,
                    "user_id": str,
                    "text": str}
        }
        return attributes

    def reload(self):
        """Function to reload saved objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.all_classes()[val["__class__"]](**val)
                            for k, val in obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            pass

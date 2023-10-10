#!/usr/bin/python3
"""
Module - base_model
Defines all common attributes and methods for other classes.
"""


import uuid
import datetime


class BaseModel:
    """Initialize a BaseModel class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    
    def __str__(self):
        """Returns a string represantion"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with current datetime"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing key/values of dict instance"""
        
        # Create a dictionary from the instance attributes
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        # Converted the datetime using ISO format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict


base = BaseModel()
model_json = base.to_dict()
print(model_json)

for key in model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(model_json[key]), model_json[key]))
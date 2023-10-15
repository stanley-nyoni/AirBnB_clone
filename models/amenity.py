#!/usr/bin/python3
"""An amenity class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """a class that manages amenity objects"""

    name = ""

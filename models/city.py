#!/usr/bin/python3
"""Defines a city class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that manages the city objects"""

    state_id = ""
    name = ""

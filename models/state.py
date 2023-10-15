#!/usr/bin/python3
"""Defines a state class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """A class that manages state objects"""

    name = ""

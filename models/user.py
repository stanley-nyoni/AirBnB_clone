#!/usr/bin/python3
"""Defines a user class that inherits from BaseModel"""
from models.base_bodel import BaseModel


class User(BaseModel):
    """Class that manages user objects"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
"""Defines a class review that inherist from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class that manages review objects"""
    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""Initializes the python package"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

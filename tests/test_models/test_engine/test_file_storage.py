#!/usr/bin/python3
"""Module - test_file_storage
   Test cases for FileStorage class
"""


import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for file_storage"""
    
    def setUp(self):
        """
           Setting up initial conditions and 
           files needed for the test
        """

        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj = BaseModel()
        self.obj.save()

    def test_file_storage_new(self):
        """Verify that the new method correctly adds an object to __objects"""
        self.assertIn(f"BaseModel.{self.obj.id}", self.storage._FileStorage__objects)


    def test_file_storage_all(self):
        """Check if the all method returns the valid __objects dictionary"""
        all_objs = self.storage.all()
        self.assertEqual(all_objs, self.storage._FileStorage__objects)

    def test_file_storage_save_with_args(self):
        """Checks save when none argument is passed"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_non_existent_file(self):
        """Ensure no exception is raised when trying to reload a non-existent file"""
        self.storage._FileStorage__file_path = "non_existent_file.json"
        self.storage.reload()

    def tearDown(self):
        """Remove the test_file.json"""

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
The ``test_file_storage`` module
==============================
Using ``test_file_storage'``
-------------------------
This is a test_file_storage unittest file to test the file_storage module.
"""
import unittest
from models import storage


class TestFileStorage(unittest.TestCase):
    """ class for testing State class"""
    def test_dict(self):
        """test if all return dictionary"""
        obj = storage.all()
        self.assertEqual(type(obj), dict)

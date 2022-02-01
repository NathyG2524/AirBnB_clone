#!/usr/bin/python3
"""
The ``test_state`` module
==============================
Using ``test_review``
-------------------------
This is a test_review unittest file to test the review module.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """ class for testing Review class"""

    def test_subclaass(self):
        """test if instance of this class is subclass of BaseModel"""
        inst_n = Review()
        self.assertTrue(issubclass(inst_n.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        inst_n = Review()
        self.assertTrue('id' in inst_n.__dict__)
        self.assertTrue('created_at' in inst_n.__dict__)
        self.assertTrue('updated_at' in inst_n.__dict__)

    def test_uuid(self):
        """check if id is str"""
        inst_n = Review()
        self.assertIs(type(inst_n.id), str)

    def test_created_at(self):
        """Tests if type of created_at is datetime."""
        inst_n = Review()
        self.assertEqual(type(inst_n.created_at), datetime)

    def test_str(self):
        """test if str method has the correct output"""
        inst_n = Review()
        string_rep = "[Review] ({}) {}".format(inst_n.id, inst_n.__dict__)
        self.assertEqual(string_rep, str(inst_n))

    def test_updated_at(self):
        """Tests if type of created_at is datetime."""
        inst_n = Review()
        self.assertEqual(type(inst_n.updated_at), datetime)

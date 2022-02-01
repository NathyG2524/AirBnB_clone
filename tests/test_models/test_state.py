#!/usr/bin/python3
"""
The ``test_state`` module
==============================
Using ``test_state``
-------------------------
This is a test_state unittest file to test the state module.
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """ class for testing State class"""

    def test_subclaass(self):
        """test if instance of this class is subclass of BaseModel"""
        inst_n = State()
        self.assertTrue(issubclass(inst_n.__class__, BaseModel), True)

    def test_has_attributes(self):
        """check that instance has all class attributes"""
        inst_n = State()
        self.assertTrue('id' in inst_n.__dict__)
        self.assertTrue('created_at' in inst_n.__dict__)
        self.assertTrue('updated_at' in inst_n.__dict__)

    def test_uuid(self):
        """check if id is str"""
        inst_n = State()
        self.assertIs(type(inst_n.id), str)

    def test_created_at(self):
        """Tests if type of created_at is datetime."""
        inst_n = State()
        self.assertEqual(type(inst_n.created_at), datetime)

    def test_str(self):
        """test if str method has the correct output"""
        inst_n = State()
        string_rep = "[State] ({}) {}".format(inst_n.id, inst_n.__dict__)
        self.assertEqual(string_rep, str(inst_n))

    def test_updated_at(self):
        """Tests if type of created_at is datetime."""
        inst_n = State()
        self.assertEqual(type(inst_n.updated_at), datetime)

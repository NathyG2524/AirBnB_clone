#!/usr/bin/python3
"""
The ``test_base_model`` module
==============================
Using ``test_base_model``
-------------------------
This is a test_base_model unittest file to test the base_model module.
"""
from models.base_model import BaseModel
from  datetime import datetime
import unittest


class TestBaseModelDocs(unittest.TestCase):
    def test_uuid(self):
        """check if id is str"""
        u_id = BaseModel()
        self.assertIs(type(u_id.id), str)

    def test_created_at(self):
        """Tests if type of created_at is datetime."""
        ins_n = BaseModel()
        self.assertEqual(type(ins_n.created_at), datetime)

    def test_str(self):
        """test if str method has the correct output"""
        ins_n = BaseModel()
        string_rep = "[BaseModel] ({}) {}".format(ins_n.id, ins_n.__dict__)
        self.assertEqual(string_rep, str(ins_n))

    def test_updated_at(self):
        """Tests if type of created_at is datetime."""
        ins_n = BaseModel()
        self.assertEqual(type(ins_n.updated_at), datetime)

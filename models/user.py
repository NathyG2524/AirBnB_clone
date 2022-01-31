#!usr/bin/pyhton3
"""
User class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """class that represents a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

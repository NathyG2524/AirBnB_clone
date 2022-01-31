#!usr/bin/pyhton3
"""
city  class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class that represents city"""
    state_id = ""
    name = ""

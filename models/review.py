#!usr/bin/pyhton3
"""
Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """detail of Review """
    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""Student Class"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """Initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns"""
        return self.__dict__

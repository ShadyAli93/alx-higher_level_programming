#!/usr/bin/python3
"""This module"""


def inherits_from(obj, a_class):
    

    """returns"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)

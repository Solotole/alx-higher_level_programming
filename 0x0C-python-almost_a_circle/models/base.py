#!/usr/bin/python3
"""Base represenation"""
import json


class Base:
    """Base class represenation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class instantiation

        Args:
            id (int): id object attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string conversion

        Args:
            list_dictionaries (list): lsit of dictionaries
            to be converted into json string

        Returns:
            return json string of the list or empty list
        """
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method to writes json atring to a file

        Args:
            List_objs (list): list of dictionaries
        """
        # dictionary = {}
        new_list = []
        if list_objs is None:
            with open("Rectangle.json", "w") as file1:
                file1.write(Base.to_json_string([]))
        elif list_objs is not None:
            for obj in list_objs:
                if isinstance(obj, Base):
                    new_list.append(obj.to_dictionary())
                with open("Rectangle.json", "w") as file1:
                    file1.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """method to returns list of json tring representation

        Args:
            json_string (str): json string represenation of list

        Returns:
            return list of json represenation
        """
        if json_string is None or len(json_string) == 0:
            lists = Base.to_json_string([])
            return json.loads(lists)
        else:
            return json.loads(json_string)

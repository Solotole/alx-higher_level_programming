#!/usr/bin/python3
"""This module represents a file storage functionality"""
import json
import os


class FileStorage:
    """Storage Class representation"""
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """Method thatt deals with returning the __objects

        Returns:
            return __objects which are the stored data dictionaries
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
            
            Args:
                obj (dictionary): instance dictionary to be set
        """
        value = ""
        identity = ""
        # for unique_id in obj.keys():
            if unique_id == "id":
                identity = obj[unique_id]
                break
        if isinstance(obj, BaseModel):
            value = str(BaseModel) + "." + identity
            FileStorage.__objects[value] = obj
            self.save()

    def save(self):
        """Method that serializes and saves the json string
            to the file path
        """
        string = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, "w") as jstring:
            jstring.write(string)

    def reload(self):
        """Deserializing json string in __file_path to __objects if
            __file_path exists and no error raised otherwise
        """
        dictionary = ""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as data:
                dictionary = data.read()
            FileStorage.__objects = json.loads(dictionary)
        else:
            pass

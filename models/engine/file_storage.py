#!/usr/bin/python3
"""this module define the file_engine class"""


import json

class FileStorage:
    """this class is used to serilze/desirile classes"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the privete __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """ add a key to an object """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes an object to JSON """

        dic = {}
        for key, obj in FileStorage.__objects.items():
            dic[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(dic, f)

    def reload(self):
        """ Deserializes a JSON file """

        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name = obj_dict['__class__']
                    obj = globals()[class_name](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

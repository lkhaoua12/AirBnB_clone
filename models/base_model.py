#!/usr/bin/python3
"""this module define the base model calss"""


import uuid
from datetime import datetime


class BaseModel:
    """base model calss of the project"""

    def __init__(self, *args, **kwargs):
        """method to call when a new instance is initilized"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, 
                    "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation of the class"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """update the date of the updated_at instance variable"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary representation of the class"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

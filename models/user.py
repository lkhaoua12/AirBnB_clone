#!/usr/bin/python3
""" this module define the user class """


from models.base_model import BaseModel

class User(BaseModel):
    """user class deifinition"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ method to initialize new user instance """
        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """ returns the string representation of the user class """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

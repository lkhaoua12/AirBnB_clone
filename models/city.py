#!/usr/bin/python3
""" this module defines the city class """


from models.base_model import BaseModel

class City(BaseModel):
    """ definition of city class """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ method to initialize new city instance """

        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """ returns the string representation of the city calss """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

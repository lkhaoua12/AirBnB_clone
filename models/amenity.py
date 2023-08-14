#!/usr/bin/python3
""" this module define the amenity class """


from models.base_model import BaseModel

class Amenity(BaseModel):
    """ definition of the amenetiy class """

    name = ""

    def __init__(self, *args, **kwargs):
        """ method to initialize a new amenetiy instance """

        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """returns the string representation of the amenity"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

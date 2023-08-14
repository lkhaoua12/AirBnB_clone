#!/usr/bin/python3
""" this module define the state class """


from models.base_model import BaseModel

class State(BaseModel):
    """ definition of the state class """

    name = ""

    def __init__(self, *args, **kwargs):
        """ mehtod to initilize a new state instance"""

        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """returns the string representation of the state"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
    

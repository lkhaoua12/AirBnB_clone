#!/usr/bin/python3
""" this module define the review class """


from models.base_model import BaseModel


class Review(BaseModel):
    """ definition of the review class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ method to initilize instance of the review class """

        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """returns the string representation of the review"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

#!/usr/bin/python3
""" this module defines Place class """


from models.base_model import BaseModel

class Place(BaseModel):
    """ difinition of Place class"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ method to initialize a new instance of the place class """

        super().__init__(self, *args, **kwargs)

    def __str__(self):
        """returns the string representation of the place"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

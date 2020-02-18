#!/usr/bin/python3

import uuid
import datetime
import json


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        __init__
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key is not '__class__':
                    setattr(self, key, value)
            self.__class__.__name__ = kwargs['__class__']
            self.created_at = datetime.datetime.strptime(kwargs['created_at'],
                                                         time_format)
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],
                                                         time_format)
        else:
            """storage.new(self)"""

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
            """
            update the update_at with the current datetime
            """
            self.updated_at = datetime.datetime.now()

    def to_dict(self):
            """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
            """
            dictt = {}
            for key, value in self.__dict__.items():
                dictt[key] = value
            dictt['created_at'] = self.created_at.isoformat()
            dictt['updated_at'] = self.updated_at.isoformat()
            dictt['__class__'] = self.__class__.__name__
            return dictt

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if ("updated_at" in dupe):
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe

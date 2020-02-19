#!/usr/bin/python3
"""
module
"""
import uuid
from datetime import datetime
import json
import models


class BaseModel():
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        __init__
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                elif key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

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
            self.updated_at = datetime.now()
            models.storage.save()

    def to_dict(self):
            """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
            """
            dictt = {}
            for key, value in self.__dict__.items():
                if key == 'created_at':
                    dictt[key] = self.created_at.isoformat()
                elif key == 'updated_at':
                    dictt[key] = self.updated_at.isoformat()
                else:
                    dictt[key] = value
            dictt['__class__'] = self.__class__.__name__
            return dictt

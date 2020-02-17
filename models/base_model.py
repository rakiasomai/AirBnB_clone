#!/usr/bin/python3

import uuid
from datetime import datetime, date, time


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        __init__
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        return("[<{}>] (<{}>) <{}>".format(self.__class__.__name__,
                                           self.id, self.__dict__))

    def save(self):
            """
            update the update_at with the current datetime
            """
            self.updated_at = datetime.now()

    def to_dict(self):
            """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
            """
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            dictt = self.__dict__ 
            dictt['__class__'] = self.__class__.__name__
            return self.__dict__

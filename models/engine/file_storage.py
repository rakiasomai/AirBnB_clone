#!/usr/bin/python3
"""
Define: FileStorage Class
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an File Storage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retreive all class instances objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """Create new Object
        """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Save new model
        """
        to_store = {obj: FileStorage.__objects[obj].to_dict(
        ) for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(to_store, f, indent=2)

    def reload(self):
        """Reload data from json file
        """
        try:
            with open(FileStorage.__file_path) as f:
                data = json.load(f)
                for i in data.values():
                    cl_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cl_name)(**i))
        except Exception:
            pass

#!/usr/bin/python3
"""
Define: FileStorage Class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        
        to_store = {obj: FileStorage.__objects[obj].to_dict(
        ) for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "a", encoding="utf-8") as f:
            json.dump(to_store, f, indent=2)"""
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
            with open(self.__file_path, mode='w', encoding="utf-8") as f:
                f.write(json.dumps(d))

    def reload(self):
        """Reload data from json file
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for i in data.values():
                    cl_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cl_name)(**i))
        except Exception:
            pass

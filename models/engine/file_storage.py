#!/usr/bin/python3
'''
Def: Class storage
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''Representing file Storage.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Retreive all class instances objects
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''Creating a new Object
        '''
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        '''def save
        '''
        to_store = {obj: FileStorage.__objects[obj].to_dict(
        ) for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(to_store, f, indent=2)

    def reload(self):
        '''Reload data
        '''
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for i in data.values():
                    cl_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cl_name)(**i))
        except Exception:
            pass

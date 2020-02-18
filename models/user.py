#!/usr/bin/python3
'''
Def: User class.
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''de class User.
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

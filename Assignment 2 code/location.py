#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Location:
    def __init__(self, id: int, name: str):
        # Initializing the Location object with provided attributes
        self.__id = id  # ID of the location
        self.name = name  # Name of the location

    def get_id(self) -> int:
        # Getter method for retrieving the ID of the location
        return self.__id

    def get_name(self) -> str:
        # Getter method for retrieving the name of the location
        return self.name

    def set_name(self, name: str) -> None:
        # Setter method for setting the name of the location
        self.name = name


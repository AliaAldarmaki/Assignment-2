#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ticket import Ticket  # Importing the Ticket class

class Visitor:
    def __init__(self, id: int, name: str, age: int, idCard: str = ""):
        # Initializing the Visitor object with provided attributes
        self.__id = id  # ID of the visitor
        self.name = name  # Name of the visitor
        self.age = age  # Age of the visitor
        self.idCard = idCard  # ID card of the visitor (optional, default is an empty string)
        self.ticket = None  # Initializing ticket attribute as None

    def get_id(self) -> int:
        # Getter method for retrieving the ID of the visitor
        return self.__id

    def get_name(self) -> str:
        # Getter method for retrieving the name of the visitor
        return self.name

    def get_age(self) -> int:
        # Getter method for retrieving the age of the visitor
        return self.age

    def get_idCard(self) -> str:
        # Getter method for retrieving the ID card of the visitor
        return self.idCard

    def set_ticket(self, ticket: Ticket) -> None:
        # Setter method for setting the ticket of the visitor
        self.ticket = ticket


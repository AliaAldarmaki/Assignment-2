#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date  # Importing the date class from the datetime module

class Ticket:
    def __init__(self, id: int, price: float, date: date, visitor: 'Visitor'):
        # Initializing the Ticket object with provided attributes
        self.__id = id  # ID of the ticket
        self.price = price  # Price of the ticket
        self.date = date  # Date of the ticket
        self.visitor = visitor  # Visitor associated with the ticket

    def get_id(self) -> int:
        # Getter method for retrieving the ID of the ticket
        return self.__id

    def get_price(self) -> float:
        # Getter method for retrieving the price of the ticket
        return self.price

    def get_date(self) -> date:
        # Getter method for retrieving the date of the ticket
        return self.date

    def get_visitor(self) -> 'Visitor':
        # Getter method for retrieving the visitor associated with the ticket
        return self.visitor

    def set_price(self, price: float) -> None:
        # Setter method for setting the price of the ticket
        self.price = price

    def set_date(self, date: date) -> None:
        # Setter method for setting the date of the ticket
        self.date = date


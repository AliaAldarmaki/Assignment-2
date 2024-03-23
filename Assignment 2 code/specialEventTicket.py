#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ticket import Ticket  # Importing the Ticket class

class SpecialEventTicket(Ticket):
    def __init__(self, ticket_id: int, price: float, date: date, visitor: Visitor):
        super().__init__(ticket_id, price, date, visitor)  # Calling the constructor of the superclass


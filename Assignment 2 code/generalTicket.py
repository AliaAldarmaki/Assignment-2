#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class GeneralTicket(Ticket):
    def __init__(self, ticket_id: int, price: float, date: date, visitor: Visitor):
        super().__init__(ticket_id, price, date, visitor)  # Calling the constructor of the superclass

    def calculate_final_price(self) -> float:
        # Method to calculate the final price of the general ticket
        return self.price  # Returning the price of the ticket


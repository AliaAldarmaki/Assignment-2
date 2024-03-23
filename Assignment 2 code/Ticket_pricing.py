#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ticket import Ticket  # Importing the Ticket class

class TicketPricing:
    def __init__(self):
        self.adult_price = 63.0  # Initialize adult ticket price
        self.discount_rate = 0.5  # Initialize discount rate
        self.vat_rate = 0.05  # Initialize VAT rate

    def calculate_ticket_price(self, visitor_age: int) -> float:
        """
        Calculate ticket price based on visitor's age.
        """
        if 18 <= visitor_age <= 60:
            return self.adult_price
        elif visitor_age < 18 or visitor_age >= 60:
            return 0.0  # Free ticket for children and seniors
        else:
            return 0.0  # Return 0 if age is invalid

    def apply_discount(self, price: float) -> float:
        """
        Apply discount to the ticket price.
        """
        return price * self.discount_rate

    def apply_vat(self, price: float) -> float:
        """
        Apply VAT to the ticket price.
        """
        return price + (price * self.vat_rate)

    def calculate_final_price(self, visitor_age: int) -> float:
        """
        Calculate the final ticket price including discount and VAT.
        """
        ticket_price = self.calculate_ticket_price(visitor_age)
        discounted_price = self.apply_discount(ticket_price)
        final_price = self.apply_vat(discounted_price)
        return final_price


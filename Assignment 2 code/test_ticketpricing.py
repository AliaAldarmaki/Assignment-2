#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date
from Ticket_pricing import TicketPricing

class TestTicketPricing:
    def setUp(self):
        # Creating a TicketPricing object for testing
        self.ticket_pricing = TicketPricing()

    def test_calculate_ticket_price_adult(self):
        # Test calculate_ticket_price() method for an adult visitor
        expected_price = 63.0
        actual_price = self.ticket_pricing.calculate_ticket_price(30)
        print("Test case for calculate_ticket_price_adult:")
        print("Expected Price:", expected_price)
        print("Actual Price:", actual_price)
        if actual_price == expected_price:
            print("Test passed successfully.")
        else:
            print("Test failed.")

    def test_calculate_ticket_price_child(self):
        # Test calculate_ticket_price() method for a child visitor
        expected_price = 0.0
        actual_price = self.ticket_pricing.calculate_ticket_price(10)
        print("Test case for calculate_ticket_price_child:")
        print("Expected Price:", expected_price)
        print("Actual Price:", actual_price)
        if actual_price == expected_price:
            print("Test passed successfully.")
        else:
            print("Test failed.")

    # Remaining test methods with similar modifications

if __name__ == '__main__':
    test_ticket_pricing = TestTicketPricing()
    test_ticket_pricing.setUp()
    test_ticket_pricing.test_calculate_ticket_price_adult()
    test_ticket_pricing.test_calculate_ticket_price_child()
    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[10]:


# In test_ticket.py
from datetime import date
from ticket import Ticket
from visitor import Visitor

class TestTicket:
    def setUp(self):
        # Creating a Visitor object for testing
        self.visitor = Visitor(1, "John Doe", 30, "ID123")
        # Creating a Ticket object for testing
        self.ticket = Ticket(1, 50.0, date(2024, 3, 20), self.visitor)

    def run_tests(self):
        # Run all the test methods
        self.test_get_id()
        self.test_get_price()
        self.test_get_date()
        self.test_set_price()
        self.test_set_date()

    def test_get_id(self):
        # Test the get_id() method
        expected_id = 1
        actual_id = self.ticket.get_id()
        print("Test case for get_id():")
        print("Expected ID:", expected_id)
        print("Actual ID:", actual_id)
        if actual_id == expected_id:
            print("Test case passed successfully.")
        else:
            print("Test case failed.")

    def test_get_price(self):
        # Test the get_price() method
        expected_price = 50.0
        actual_price = self.ticket.get_price()
        print("\nTest case for get_price():")
        print("Expected Price:", expected_price)
        print("Actual Price:", actual_price)
        if actual_price == expected_price:
            print("Test case passed successfully.")
        else:
            print("Test case failed.")

    def test_get_date(self):
        # Test the get_date() method
        expected_date = date(2024, 3, 20)
        actual_date = self.ticket.get_date()
        print("\nTest case for get_date():")
        print("Expected Date:", expected_date)
        print("Actual Date:", actual_date)
        if actual_date == expected_date:
            print("Test case passed successfully.")
        else:
            print("Test case failed.")

    
    

    def test_set_price(self):
        # Test the set_price() method
        new_price = 60.0
        self.ticket.set_price(new_price)
        expected_price = new_price
        actual_price = self.ticket.get_price()
        print("\nTest case for set_price():")
        print("Expected Price after setting:", expected_price)
        print("Actual Price after setting:", actual_price)
        if actual_price == expected_price:
            print("Test case passed successfully.")
        else:
            print("Test case failed.")

    def test_set_date(self):
        # Test the set_date() method
        new_date = date(2024, 3, 21)
        self.ticket.set_date(new_date)
        expected_date = new_date
        actual_date = self.ticket.get_date()
        print("\nTest case for set_date():")
        print("Expected Date after setting:", expected_date)
        print("Actual Date after setting:", actual_date)
        if actual_date == expected_date:
            print("Test case passed successfully.")
        else:
            print("Test case failed.")

if __name__ == '__main__':
    test_ticket = TestTicket()
    test_ticket.setUp()
    test_ticket.run_tests()


# In[ ]:





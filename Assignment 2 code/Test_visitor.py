#!/usr/bin/env python
# coding: utf-8

# In[10]:


from ticket import Ticket  # Importing the Ticket class
from visitor import Visitor  # Importing the Visitor class

class TestVisitor:
    def setUp(self):
        # Creating a Visitor object for testing
        self.visitor = Visitor(1, "Fatima", 30, "ID123")

    def test_get_id(self):
        # Test the get_id() method
        expected_id = 1
        actual_id = self.visitor.get_id()
        print("Test case for get_id(). Expected ID:", expected_id, "Actual ID:", actual_id)
        try:
            assert actual_id == expected_id
            print("Test case passed successfully.")
        except AssertionError:
            print("Test case failed.")

    def test_get_name(self):
        # Test the get_name() method
        expected_name = "Alia"
        actual_name = self.visitor.get_name()
        print("Test case for get_name(). Expected Name:", expected_name, "Actual Name:", actual_name)
        try:
            assert actual_name == expected_name
            print("Test case passed successfully.")
        except AssertionError:
            print("Test case failed.")

    def test_get_age(self):
        # Test the get_age() method
        expected_age = 30
        actual_age = self.visitor.get_age()
        print("Test case for get_age(). Expected Age:", expected_age, "Actual Age:", actual_age)
        try:
            assert actual_age == expected_age
            print("Test case passed successfully.")
        except AssertionError:
            print("Test case failed.")

    def test_get_idCard(self):
        # Test the get_idCard() method
        expected_idCard = "ID123"
        actual_idCard = self.visitor.get_idCard()
        print("Test case for get_idCard(). Expected ID Card:", expected_idCard, "Actual ID Card:", actual_idCard)
        try:
            assert actual_idCard == expected_idCard
            print("Test case passed successfully.")
        except AssertionError:
            print("Test case failed.")

   
    def test_set_ticket(self):
        # Creating a Ticket object for testing
        ticket = Ticket(101, 50.0, "2024-03-20", self.visitor)
        # Setting the ticket for the visitor
        self.visitor.set_ticket(ticket)
        expected_ticket = ticket
        actual_ticket = self.visitor.ticket
        print("Test case for set_ticket(). Expected Ticket ID:", expected_ticket.get_id(), "Actual Ticket ID:", actual_ticket.get_id())
        try:
            assert actual_ticket.get_id() == expected_ticket.get_id()
            print("Test case passed successfully.")
        except AssertionError:
            print("Test case failed.")


if __name__ == '__main__':
    #create the Instance
    test_visitor = TestVisitor()
    test_visitor.setUp()
    test_visitor.test_get_id()
    test_visitor.test_get_name()
    test_visitor.test_get_age()
    test_visitor.test_get_idCard()
    test_visitor.test_set_ticket()


# In[ ]:





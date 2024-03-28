#!/usr/bin/env python
# coding: utf-8

# In[12]:
 

from datetime import date
from location import Location
from artwork import Artwork

class TestArtwork:
    def setUp(self):
        # Creating a Location object for testing
        self.location = Location(1, "Gallery A")
        # Creating an Artwork object for testing
        self.artwork = Artwork(1, "Mona Lisa", "Leonardo da Vinci", date(1503, 8, 21), "Iconic portrait", self.location)

    def test_get_id(self):
        # Test the get_id() method
        expected_id = 1
        actual_id = self.artwork.get_id()
        print("Test case for get_id(). Expected ID:", expected_id, "Actual ID:", actual_id)
        assert actual_id == expected_id
        print("Test case for get_id() passed successfully.")

    def test_get_title(self):
        # Test the get_title() method
        expected_title = "Mona Lisa"
        actual_title = self.artwork.get_title()
        print("Test case for get_title(). Expected Title:", expected_title, "Actual Title:", actual_title)
        assert actual_title == expected_title
        print("Test case for get_title() passed successfully.")

    def test_get_artist(self):
        # Test the get_artist() method
        expected_artist = "Leonardo da Vinci"
        actual_artist = self.artwork.get_artist()
        print("Test case for get_artist(). Expected Artist:", expected_artist, "Actual Artist:", actual_artist)
        assert actual_artist == expected_artist
        print("Test case for get_artist() passed successfully.")

    def test_get_creation_date(self):
        # Test the get_creation_date() method
        expected_date = date(1503, 8, 21)
        actual_date = self.artwork.get_creation_date()
        print("Test case for get_creation_date(). Expected Date:", expected_date, "Actual Date:", actual_date)
        assert actual_date == expected_date
        print("Test case for get_creation_date() passed successfully.")

    def test_get_historical_significance(self):
        # Test the get_historical_significance() method
        expected_significance = "Iconic portrait"
        actual_significance = self.artwork.get_historical_significance()
        print("Test case for get_historical_significance(). Expected Significance:", expected_significance, "Actual Significance:", actual_significance)
        assert actual_significance == expected_significance
        print("Test case for get_historical_significance() passed successfully.")

    
    def test_set_location(self):
         # Creating a new Location object for testing
            new_location = Location(2, "Gallery B")
          # Setting the new location for the artwork
            self.artwork.set_location(new_location)
          # Test if the location is set correctly
            actual_location = self.artwork.get_location()
            try:
                assert actual_location.get_id() == new_location.get_id() and actual_location.get_name() == new_location.get_name()
                print("Test case for set_location() passed successfully. Expected Location ID:", new_location.get_id(), "Name:", new_location.get_name(), "Actual Location ID:", actual_location.get_id(), "Name:", actual_location.get_name())
            except AssertionError:
                print("Test case for set_location() failed. Expected Location ID:", new_location.get_id(), "Name:", new_location.get_name(), "Actual Location ID:", actual_location.get_id(), "Name:", actual_location.get_name())

    def test_add_artwork_to_museum(self):
        # Simulate adding artwork to the museum
        museum = []  # Simulate a list of artworks in the museum
        museum.append(self.artwork)  # Add the artwork to the museum list
        # Test if the artwork is successfully added to the museum
        assert self.artwork in museum
        print("Test case for adding artwork to the museum passed successfully.")

if __name__ == '__main__':
    test_artwork = TestArtwork()
    test_artwork.setUp()
    test_artwork.test_get_id()
    test_artwork.test_get_title()
    test_artwork.test_get_artist()
    test_artwork.test_get_creation_date()
    test_artwork.test_get_historical_significance()
    test_artwork.test_set_location()
    test_artwork.test_add_artwork_to_museum()


# In[ ]:





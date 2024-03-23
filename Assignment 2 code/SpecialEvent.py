#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date  # Importing the date class
from artwork import Artwork  # Importing the Artwork class
from location import Location  # Importing the Location class

class SpecialEvent(Artwork):
    def __init__(self, id: int, title: str, artist: str, creation_date: date, historical_significance: str, location: Location, event_date: date):
        """
        Represents a special event held in the museum.

        """
        super().__init__(id, title, artist, creation_date, historical_significance, location)
        self.event_date = event_date

    def getEventDate(self) -> date:
        """
        Get the date of the special event.
        """
        return self.event_date


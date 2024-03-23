#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date  # Importing the date class
from artwork import Artwork  # Importing the Artwork class
from location import Location  # Importing the Location class

class Exhibition(Artwork):
    def __init__(self, id: int, title: str, artist: str, creation_date: date, historical_significance: str, location: Location, start_date: date, end_date: date):
        """
        Represents an exhibition held in the museum.

        """
        super().__init__(id, title, artist, creation_date, historical_significance, location)
        self.start_date = start_date
        self.end_date = end_date

    def getStartDate(self) -> date:
        """
        Get the start date of the exhibition.
        """
        return self.start_date

    def getEndDate(self) -> date:
        """
        Get the end date of the exhibition.
        """
        return self.end_date


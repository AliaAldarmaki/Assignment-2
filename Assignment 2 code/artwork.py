#!/usr/bin/env python
# coding: utf-8

# In[ ]:

 
# Importing the necessary module and class
from datetime import date
from location import Location

class Artwork:
    def __init__(self, id: int, title: str, artist: str, creation_date: date, historical_significance: str, location: Location):
        # Initializing the Artwork object with provided attributes
        self.__id = id  # ID of the artwork
        self.title = title  # Title of the artwork
        self.artist = artist  # Artist who created the artwork
        self.creation_date = creation_date  # Date when the artwork was created
        self.historical_significance = historical_significance  # Historical significance of the artwork
        self.location = location  # Location where the artwork is displayed

    def get_id(self) -> int:
        # Getter method for retrieving the ID of the artwork
        return self.__id

    def get_title(self) -> str:
        # Getter method for retrieving the title of the artwork
        return self.title

    def get_artist(self) -> str:
        # Getter method for retrieving the artist of the artwork
        return self.artist

    def get_creation_date(self) -> date:
        # Getter method for retrieving the creation date of the artwork
        return self.creation_date

    def get_historical_significance(self) -> str:
        # Getter method for retrieving the historical significance of the artwork
        return self.historical_significance

    def get_location(self) -> Location:
        # Getter method for retrieving the location where the artwork is displayed
        return self.location

    def set_location(self, location: Location) -> None:
        # Setter method for setting the location where the artwork is displayed
        self.location = location


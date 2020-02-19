"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""

class LibraryItem:
    """Base class for all items stored in a library catalog

    Provides a simple LibraryItem with only a few attributes

    """

    _all_items = []

    def __init__(self, name, isbn, tags=[]):
        """Initialize a LibraryItem

        :param name: (string) Name of item
        :param isbn: (string) ISBN number for the item
        :param tags: (list) List of CategoryTags
        """
        self.name = name
        self.isbn = isbn
        self.tags = tags
        self.resource_type = 'Generic'  # This is the type of item being stored

    def match(self, filter_text):
        """True/False whether the item is a match for the filter_text

        match should be case insensitive and should search all attributes of
        the class.  Depending on the attribute, match requires an exact match or
        partial match.

        match needs to be redefined for any subclasses.  Please see the
        note/notebook case study from Chapter 2 as an example of how match
        is designed to work.

        :param filter_text: (string) string to search for
        :return: (boolean) whether the search_term is a match for this item
        """
        return filter_text.lower() in self.name.lower() or \
            filter_text.lower() == self.isbn.lower() or \
            filter_text.lower() in (str(tag).lower() for tag in self.tags)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        """
        return f'{self.name}\n{self.isbn}\n{self.resource_type}\n{", ".join(self.tags)}'

    def to_short_string(self):
        """Return a short string representation of the item

        String contains only the name of the item and the type of the item
        I.E.
        Moby Dick - eBook
        All subclasses must provide a to_short_string method
        """
        return f'{self.name} - {self.resource_type}'


class Book(LibraryItem):

    def __init__(self, name, isbn, author, tags=[]):
        super().__init__(name, isbn, tags)
        self.author = author
        self.resource_type = "Book"

    def match(self, filter_text):

        return filter_text.lower() in self.author.lower() or \
            super().match(filter_text)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        """

        return super().__str__() + f'\n{self.author}'


class DVD(LibraryItem):

    def __init__(self, name, isbn, director, actor, tags=[]):
        super().__init__(name, isbn, tags)
        self.director = director
        self.actor = actor
        self.resource_type = "DVD"

    def match(self, filter_text):
        return filter_text.lower() in self.director.lower() or \
            filter_text.lower() in self.actor.lower() or \
            super().match(filter_text)

    def __str__(self):
        return super().__str__() + f'\n{self.actor}\n{self.director}'


class MusicCD(LibraryItem):

    def __init__(self, name, isbn, artist, album, num_discs, tags):
        super().__init__(name, isbn, tags)
        self.artist = artist
        self.album = album
        self.num_discs = num_discs
        self.resource_type = "Music CD"

    def match(self, filter_text):
        return filter_text.lower() in self.artist.lower() or \
            filter_text.lower() in self.album.lower() or \
            super().match(filter_text)

    def __str__(self):
        return super().__str__() + f'\n{self.artist}\n{self.album}\n{self.num_discs}'

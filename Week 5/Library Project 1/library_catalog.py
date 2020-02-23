"""
Contains definitions for the abstract base class LibraryItem as well as CategoryTags
"""


class Catalog:
    """Base class to hold lists of library items
    """

    def __init__(self, name, _all_items=None):
        """Initialize a Catalog

        :param name: (string) Name of the catalog
        :param _all_items: (list) List of LibraryItems in the catalog. Private
        """
        self.name = name

        if _all_items:
            self._all_items = _all_items
        else:
            self._all_items = []

    def add_items(self, library_items):
        """Add a list of items to the list of all library items

        :param library_items: (list) A list of library items to add
        :return: Nothing
        """
        for item in library_items:
            self._all_items.append(item)

    def remove_items(self, library_items):
        """Remove a list of items from the catalog

        :param library_items: (list) A list of library items to remove.
        :return: Nothing
        """
        for item in library_items:
            try:
                self._all_items.remove(item)
            except ValueError:
                pass

    def search_items(self, filter_text):
        """ Search for items and add any matching items to a list

        :param filter_text: (string) The text to search for in the item's fields
        :return: A list of matching objects
        """
        output = []

        for item in self._all_items:

            if item.match(filter_text):
                output.append(item)

        return output


class LibraryItem:
    """Base class for all items stored in a library catalog

    Provides a simple LibraryItem with only a few attributes

    """

    def __init__(self, name, isbn, tags=None):
        """Initialize a LibraryItem

        :param name: (string) Name of item
        :param isbn: (string) ISBN number for the item
        :param tags: (list) List of CategoryTags
        """
        self.name = name
        self.isbn = isbn

        if tags:
            self.tags = tags
        else:
            self.tags = []
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
        return f'Name: {self.name}\nISBN: {self.isbn}\nItem Type: {self.resource_type}\nTags: {", ".join(self.tags)}\n'

    def to_short_string(self):
        """Return a short string representation of the item

        String contains only the name of the item and the type of the item
        I.E.
        Moby Dick - eBook
        All subclasses must provide a to_short_string method
        """
        return f'{self.name} - {self.resource_type}'


class Book(LibraryItem):
    """Base class for any Books
    """

    def __init__(self, name, isbn, author, tags=None):
        """
        Initialize a new book object

        :param name: (string) The name (title) of the book
        :param isbn: (string) The ISBN of the object
        :param author: (string) The name of athe author of the book.
        :param tags:  (list) A list of tags describing the book ex. ['Romance', 'Victorian']
        """
        super().__init__(name, isbn, tags)
        self.author = author
        self.resource_type = "Book"

    def match(self, filter_text):
        """An extension of the match function in the base LibraryItem class.

        Also searches for the filter text in the author variable.

        :param filter_text: (string) The text to search for
        :return: A boolean true false value for whether the filter text was in any of the locations
        """

        return filter_text.lower() in self.author.lower() or \
            super().match(filter_text)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method

        :return: A well formatted string reprsentation fo the item
        """

        return super().__str__() + f'\nAuthor: {self.author}'


class DVDMovie(LibraryItem):
    """Base class for any DvDs
    """

    def __init__(self, name, isbn, director, actor, tags=None):
        """ Initialize a DVDMovie Item

        :param name: (string) The name of the DVD
        :param isbn: (string) The ISBN of the DVD
        :param director: (string) The director of the movie
        :param actor: (string) The lead actor in the movie
        :param tags: (list) A list of tags describing the movie content. ex. ["Christmas", "Action", "Robbery"]
        """
        super().__init__(name, isbn, tags)
        self.director = director
        self.actor = actor
        self.resource_type = "DVD"

    def match(self, filter_text):
        """An extension of the LibraryItem's match method. Also searches for filter text in the director and actor
        fields.

        :param filter_text: (string) The text to search for
        :return: A boolean true or false value for whether the variable was found
        """

        return filter_text.lower() in self.director.lower() or \
            filter_text.lower() in self.actor.lower() or \
            super().match(filter_text)

    def __str__(self):
        """Return a well formatted string representation of the item

        All instance variables are included.

        All subclasses must provide a __str__ method
        :return: A well formatted string representation of the item
        """
        return super().__str__() + f'Lead Actor: {self.actor}\nDirector: {self.director}\n'


class MusicCD(LibraryItem):
    """ Base class for any music CDs
    """

    def __init__(self, name, isbn, artist, num_discs, tags=None):
        """ Initialize a MusicCD item.

        :param name: (string) The name of the MusicCD
        :param isbn: (string) The ISBN number of the CD
        :param artist: (string) The recording artist for the MusicCD
        :param num_discs: (int) The number of discs in the case
        :param tags: (list) A list of tags describing the item. ex. ["60s", "British", "Rock"]
        """

        super().__init__(name, isbn, tags)
        self.artist = artist
        self.num_discs = num_discs
        self.resource_type = "Music CD"

    def match(self, filter_text):
        """ An extension of the Library Item's match method. Also searches for the filter text in the artist variable

        :param filter_text: (string) The text being searched for
        :return: A boolean true or false for whether there was a match or not.
        """

        return filter_text.lower() in self.artist.lower() or \
            super().match(filter_text)

    def __str__(self):
        return super().__str__() + f'Recording Artist: {self.artist}\nNumber of Discs: {self.num_discs}\n'

"""Implements the functions created in library_catalog.py and allows you to add/remove items to a catalog,
print catalog contents, and search for specific catalog items.

Author: John Shultz
Class: CSI-260-03
Assignment: Library Project Part 2
Due Date: 2/28/2019 12:30 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
from library_catalog import LibraryItem, DVDMovie, MusicCD, Book, Catalog, CategoryTag

# Create a catalog named catalog that we will work with.
catalog = Catalog("Champlain College Library Catalog")


def tagadd():
    """A function to handle adding tags without creating tags with duplicate names

    :return: A list of tags to add to a new object.
    """

    tags = []
    while True:
        new_tag = str(input("Enter in the name of the new tag ex. nonfiction: "))

        # Check to see if new_tag is not empty
        if new_tag:
            # If the new tag is not in the list of all tag names, create a tag with that name and add it
            # to list
            if new_tag.lower() not in CategoryTag.all_category_tags().split():
                tags.append(CategoryTag(new_tag))

            # If there is a tag with that name, simply find the tag with the matching name and add that tag
            # instead.
            else:
                for tag in CategoryTag._all_tags:
                    if tag.name == new_tag.lower():
                        tags.append(tag)
        else:
            return tags


def search_catalog():
    """UI for searching the catalog"""
    filter_text = str(input("Enter in some text to search for (name, author, director, tag, etc.): "))
    while True:
        print("1. Book\n2. DVD Movie\n3. Music CD")
        type_filter = input("Enter in one of the above choices to filter by item or nothing to show all items: ")
        if type_filter in ["1", "2", "3", ""]:
            break
        else:
            print("Please only enter in a valid choice or no input.")

    print('Searching the catalog')

    filter_dict = {"1": "Book", "2": "DVD", "3": "Music CD"}

    # Call the Catalog.search_items function which returns a list of matching items
    if type_filter:
        found_items = catalog.search_items(filter_text, filter_dict[type_filter])
    else:
        found_items = catalog.search_items(filter_text)

    print("Here are your results!")
    print("---------------------")

    # Check to see if any items were found. If any were, print each found item to screen
    if found_items:
        for item in found_items:
            print(item)


def print_catalog():
    """Prints the contents of the catalog neatly

    :return: Nothing
    """

    print("Here all all the items in the library catalog!")
    print("----------------------------------------------")

    for item in catalog._all_items:
        print(item)


def add_item():
    """Adds a list of items to the catalog

    :return: No return value, but appends a list of items to catalog._all_items
    """

    new_items = []

    while True:
        print("1. Book")
        print("2. DVD Movie")
        print("3. Music CD")

        try:
            item_choice = int(input("Enter a number to select the type of item you want to add: "))

            if item_choice == 1:
                # Make a book
                name = str(input("Enter the name of the book: "))
                isbn = str(input("Enter the ISBN of the book: "))
                author = str(input("Enter the author of the book: "))
                tags = tagadd()
                new_book = Book(name, isbn, author, tags)
                new_items.append(new_book)

            elif item_choice == 2:
                # Make a DVD movie
                name = str(input("Enter the name of the DVD: "))
                isbn = str(input("Enter the ISBN of the DVD: "))
                director = str(input("Enter in the director of the movie: "))
                actor = str(input("Enter in the lead actor in the movie: "))
                tags = tagadd()
                new_dvd = DVDMovie(name, isbn, director, actor, tags)
                new_items.append(new_dvd)

            elif item_choice == 3:
                # Make a Music CD
                name = str(input("Enter the name of the CD: "))
                isbn = str(input("Enter the ISBN of the CD: "))
                artist = str(input("Enter in the recording artist of the CD: "))

                while True:
                    try:
                        num_discs = int(input("Please enter in the number of discs: "))
                        break

                    except ValueError:
                        print("That's not a valid number!")

                tags = tagadd()
                new_cd = MusicCD(name, isbn, artist, num_discs, tags)
                new_items.append(new_cd)

            else:
                print("Please enter one of the above numbers")

            run_again = str(input("Would you like to add another item (Y/N): "))

            if run_again.lower() not in ['y', 'yes']:
                catalog.add_items(new_items)
                break

        except ValueError:
            print("Please enter one of the above numbers")


def remove_item():
    """Takes an item with a given name and removes it from the catalog

    :return: nothing. Removes entries from catalog._all_items
    """

    remove_name = str(input("Enter the name of the item you wish to remove: "))

    for item in catalog._all_items:
        if item.name.lower() == remove_name.lower():
            print(f'Removing a {item.resource_type} named {item.name}')
            catalog.remove_items([item])


def save_catalog():
    """Saves a .picle archive of the catalog's _all_items variable

    :return:
    """
    file_name = str(input('Enter in the filename or filepath you want to save the file to, excluding extension: '))
    catalog.save_catalog(file_name)


def load_catalog():
    """Loads a .pickle archive the catalog's _all_items variable

    :return: Nothing
    """
    file_name = str(input('Enter in filename or filepath of pickle file to load from, excluding extension: '))

    catalog.load_catalog(file_name)


catalog_menu = """Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add items to catalog
4. Remove items from catalog
5. Save the contents of the catalog
6. Load a pickle archived catalog.

Choose an option: """


menu_options = {'1': search_catalog,
                '2': print_catalog,
                '3': add_item,
                '4': remove_item,
                '5': save_catalog,
                '6': load_catalog}

while True:
    user_choice = input(catalog_menu)
    if user_choice in menu_options:
        menu_options[user_choice]()
    else:
        print('That option is not recognized')

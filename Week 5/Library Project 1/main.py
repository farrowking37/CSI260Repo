from library_catalog import LibraryItem, DVDMovie, MusicCD, Book, Catalog


def search_catalog(catalog, filter_text):
    """UI for searching the catalog"""
    print('Searching the catalog')

    # Call the Catalog.search_items function which returns a list of matching items
    found_items = catalog.search_items(filter_text)

    # Check to see if any items were found. If any were, print each found item to screen
    if found_items:
        for item in found_items:
            print(item)


def print_catalog(catalog):

    print("Here all all the items in the library catalog!")

    for item in catalog._all_items:
        print(item)


def add_item(catalog):

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
                isbn = str(input("Enter the ISBN of the book"))
                author = str(input("Enter the author of the book"))
                tags = []
                while True:
                    new_tag = str(input("Enter in a tag describing the book, or nothing to quit: "))

                    if new_tag:
                        tags.append(new_tag)
                    else:
                        break

                new_book = Book(name, isbn, author, tags)
                new_items.append(new_book)


            if item_choice == 2:
                # Make a DVD Movie
                pass
            if item_choice == 3:
                # Make a Music CD
                pass

        except ValueError:
            print("Please enter one of the above numbers")


def remove_item():
    pass
    # Todo Complte Function


catalog_menu = """Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add items to catalog
4. remove items from catalog
5. Open catalog from file
6. Save catalog to file

Choose an option: """


menu_options = {'1': search_catalog,
                '2': print_catalog,
                '3': add_item,
                '4': remove_item}

while True:
    user_choice = input(catalog_menu)
    if user_choice in menu_options:
        menu_options[user_choice]()
    else:
        print('That option is not recognized')

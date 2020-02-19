from library_catalog import LibraryItem

def search_catalog():
    """UI for searching the catalog"""
    print('Searching the catalog')
    # Todo Complete function


def print_catalog():
    print('printing the catalog')
    # Todo Complete function


catalog_menu = """Library Catalog Menu

1. Search catalog
2. Print the entire catalog
3. Add items to catalog
4. remove items from catalog
5. Open catalog from file
6. Save catalog to file

Choose an option: """


menu_options = {'1': search_catalog,
                '2': print_catalog}

while True:
    user_choice = input(catalog_menu)
    if user_choice in menu_options:
        menu_options[user_choice]()
    else:
        print('That option is not recognized')

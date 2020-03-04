"""
This file contains notes taken during my week 8 python class. Taken inside a .py file so any example python code can be
executed.
"""
import phonenumbers
import zipcodes


class ExampleClass:

        def __str__(self):
            """This is used to return the informal string version of the object

            :return: The informal string version of the object
            """

        def __repr__(self):
            """This is used to return the formal string version of an object

            :return: The formal string version of the object
            """

            # In general, should return more information than string, enough to identify a specific item.


# The below code shows examples of using properties in python
class Patient:
    """An individual patient"""

    def __init__(self, first, middle, last, address, city, state, zip_code, phone,
                 em_contact, em_phone):
        """
        Initialize a patient
        :param first: (string)
        :param middle: (string)
        :param last: (string)
        :param address: (string)
        :param city: (string)
        :param state: (string)
        :param zip_code: (string)
        :param phone: (string)
        :param em_contact: (string)
        :param em_phone: (string)
        """
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.em_contact = em_contact
        self.em_phone = em_phone

    def __str__(self):
        """Returns patient as a nicely formatted string"""
        return f'First: {self.first}\n' \
            f'Middle: {self.middle}\n' \
            f'Last: {self.last}\n' \
            f'Address: {self.address}\n' \
            f'City: {self.city}\n' \
            f'State: {self.state}\n' \
            f'Zip Code: {self.zip_code}\n' \
            f'Phone: {self.phone}\n' \
            f'Emergency Contact: {self.em_contact}\n' \
            f'Emergency Phone: {self.em_phone}\n'


    @property
    def em_phone(self):
        return phonenumbers.format_number(self._em_phone, phonenumbers.PhoneNumberFormat.NATIONAL)

    @em_phone.setter
    def em_phone(self, new_number):
        self._em_phone = phonenumbers.parse(new_number, "US")

    @property
    def phone(self):
        return phonenumbers.format_number(self._phone, phonenumbers.PhoneNumberFormat.NATIONAL)

    @phone.setter
    def phone(self, new_number):
        self._phone = phonenumbers.parse(new_number, "US")

    @property
    def full_name(self):
        return f'{self.first} {self.middle} {self.last}'

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code):

        # Raise TypeError if the provided code is not a valid zip code
        if zipcodes.is_real(new_zip_code):
            self._zip_code = new_zip_code
        else:
            raise TypeError(f'{new_zip_code} is not a valid zip code')


if __name__ == '__main__':
    john_doe = Patient('John', 'Samuel', 'Doe', '111 North St.', 'Burlington',
                       'VT', '05401', '8025559889', 'Mary Doe', '8025559889')
    print(john_doe)
    print(john_doe.full_name)
    print(john_doe.zip_code)
"""This Module conatins the classes of Patient and Procedue, designed to track information about patients and the
procedures they will be undergoing.

Author: John Shultz
Class: CSI-260-03
Assignment: Week 4 Lab
Due Date: February 13, 2020 11:59 PM

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
import pickle


class Patient:
	# Private class variable _all_patients
	_all_patients = dict()

	# Private class variable _next_id
	_next_id = 1

	def __str__(self):
		"""When converted to string, prints out all information about patient.

		:return: An empty string to prevent errors. Do not use print(Patient), instead use str(Patient) for same purpose
		"""
		print(f'Name: {self.name}')
		print(f'Age: {self.age}')
		print(f'Gender: {self.gender}')
		print(f'Height: {self.height}')
		print(f'Weight: {self.weight}')
		print("---Upcoming Procedures---")
		for procedure in self.procedures:
			print(str(procedure))
		print("---Contacts---")
		for contact in self.contact_list.items():
			print(f'{contact[0]}: {contact[1]}')

		return ""

	def __init__(self, name, age, gender, height, weight, contact_list=dict()):
		"""Initialize a new Patient

		:param name: (str) The name of the patient.
		:param age: (int) the age of the patient
		:param gender: (str) The gender of the patient
		:param height: (str) The height of the patient ex. 5'8"
		:param weight: (int) The patient's weight in lbs
		:param contact_list: (dict) A dictionary of contact numbers. ex. {'Cell': "123-456-7890", "Mom": "555-555-5555"}
		"""

		# Set the patient's id to the next ID, and then increment the value of next id.
		self._id = Patient._next_id
		Patient._next_id += 1

		# Add the new patient to the dictionary of patients, indexed by it's ID
		Patient._all_patients[self._id] = self

		# Assign the values of other patient properties to instance variables.
		self.name = name
		self.age = age
		self.gender = gender
		self.height = height
		self.weight = weight
		self.contact_list = contact_list

		# Create an empty list to store procedures
		self.procedures = []

	# Appends the procedure to the procedure list.
	def add_procedure(self, procedure):
		"""Adds a procedure to the patient's procedure list.

		:param procedure: (Procedure) The procedure to be added
		:return: Nothing. Modifies instance variable procedures.
		"""
		self.procedures.append(procedure)

	@staticmethod
	def get_patient(patient_id):
		"""Returns a patient object with the given ID number.

		:param patient_id: (int) The requested Patient ID
		:return: If patient found, returns the Patient object. Otherwise, returns nothing.
		"""

		# Tries to return the patient with that given ID. Catches exception if there is no patient, returns None.
		try:
			return Patient._all_patients[patient_id]
		except KeyError:
			return None

	@staticmethod
	def delete_patient(patient_id):
		"""Deletes a patient from the list of all patients

		:param patient_id: (int) The ID of the patients that should be delted
		:return: Nothing. Modifies class variable _all_patients
		"""

		# Try to delete the given ID from the list of all patients. If it exists, delete it. If not, do nothing.
		try:
			del Patient._all_patients[patient_id]
		except KeyError:
			pass

	@staticmethod
	def save_patients(file_name):
		"""Create a pickle file containing a tuple of the _all_patients dictionary and the _next_id value

		:param file_name: (str) The desired file path and name for the pickle file. No file extension should be included
		:return: Nothing. Saves a pickle file to the user's drive at the path listed in file_name
		"""
		pickle.dump((Patient._all_patients, Patient._next_id), open(f'{file_name}.p', 'wb'))

	@staticmethod
	def load_patients(file_name):
		"""Loads the _all_patients dictionary and _next_id values from a pickle file and saves them to class variables.

		:param file_name: (str) The desired file path and name for the pickle file. No file extension should be included
		:return: Nothing. Either loads file or prints file not found.
		"""
		try:
			Patient._all_patients, Patient._next_id = pickle.load(open(f'{file_name}.p', 'rb'))
		except FileNotFoundError:
			print("No file with that name found!")


class Procedure:
	_next_id = 1

	def __str__(self):
		"""Creates the string that is returned when you cast a procedure to a string.

		:return: An f-string containing all information about a procedure.
		"""

		return f'On {self.date} {self.doctor} will perform {self.name} at {self.location}'

	def __init__(self, name, doctor, location, date):
		"""Initializes a new Procedure

		:param name: (str) The name of the procedure. ex. Yearly Checkup
		:param doctor: (str) The name of the medical professional performing the procedure
		:param location: (str) The location the procedure will be performed at. ex. 123 Fake Street ex2. Main Office
		:param date: (str) The date the procedure will be performed ex. 1/1/1970
		"""

		# Set the ID of the procedure to the next ID.
		self._id = Procedure._next_id

		# Assign other values based on user input
		self.name = name
		self.doctor = doctor
		self.location = location
		self.date = date

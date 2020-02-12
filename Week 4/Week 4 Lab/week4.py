"""This Module serves as the CLI for the classes contained within medical.py

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
from medical import Patient, Procedure

print("Hi! Welcome to the patient management tool! Before we can begin, we need to load the patient_info.")
file_name = str(input("Plese enter in the full file path and name without extension where we can find this file: "))

Patient.load_patients(file_name)

while True:
	print("--Main Menu--")
	print("1. Look up a Patient by ID")
	print("2. Add a new Patient")
	print("3. Quit")

	# Take the users main menu option. Except any non number answers
	try:
		user_choice = int(input("Please enter in the number you would like to select: "))

		if user_choice == 1:
			patient_id = int(input("Please enter in the patient ID number: "))
			current_patient = Patient.get_patient(patient_id)

			# If there was no patient with that ID, current patient will store None and evaluate as false.
			if current_patient:

				# Print all the patient info, as well as a list of patient options
				str(current_patient)
				print("1. Change Name")
				print("2. Change Age")
				print("3. Change Gender")
				print("4. Change Height")
				print("5. Change Weight")
				print("6. Add or Modify Contact")
				print("7. Remove Contact")
				print("8. Add Procedure")
				print("9. Delete Patient")
				print("10. Do Nothing")

				# Try to take in the user's choice and perform the action. Catch non-number choices and except them.
				try:
					patient_choice = int(input("Please enter in which option you would like to perform: "))

					# Change Name
					if patient_choice == 1:
						current_patient.name = str(input("Please enter in the new name for the patient: "))

					# Change Age
					elif patient_choice == 2:
						current_patient.age = int(input("Please enter in the new age for the patient: "))

					# Change gender
					elif patient_choice == 3:
						current_patient.gender = str(input("Please enter in the new gender for the patient: "))

					# Change height
					elif patient_choice == 4:
						current_patient.height = str(input("Please enter the new height for the patient: "))

					# Change Weight
					elif patient_choice == 5:
						current_patient.weight = int(input("Please enter the new weight in lbs for the patient: "))

					# Add or Modify a contact number
					elif patient_choice == 6:
						contact = str(input("Please enter in the label for the new contact or contact to be modified"))
						number = str(input("Please enter in the new number"))
						current_patient.contact_list[contact] = number

					# Remove Contact
					elif patient_choice == 7:

						# Print out a list of all currently saved contacts
						for contact in current_patient.contact_list.keys():
							print(contact)

						# Delete the contact of the user's choice.
						contact = str(input("Which of the above contacts would you like to delete?"))
						del current_patient.contact_list[contact]

					# Add procedure
					elif patient_choice == 8:
						procedure_name = str(input("Please enter the name of the procedure: "))
						procedure_doctor = str(input("Please enter the name of the doctor performing the procedure: "))
						procedure_location = str(input("Please enter where this procedure will be performed: "))
						procedure_date = str(input("Please enter the date this procedure will be performed: "))
						new_procedure = Procedure(procedure_name, procedure_doctor, procedure_location, procedure_date)
						current_patient.add_procedure(new_procedure)

					# Delete Patient
					elif patient_choice == 9:

						# Check to make sure user is sure, if they are, call delete patient function.
						accident_check = str(input("Are you sure (Y/N): "))
						if accident_check.upper() == "Y" or accident_check.upper() == "YES":
							Patient.delete_patient(patient_id)

					# Do Nothing
					elif patient_choice == 10:
						pass

					# If the user makes a non numbered choice, send them to main menu
					else:
						print("That was not a valid choice! Returning to main menu.")

				except ValueError:
					print("That is not a valid number! Returning to main menu.")
			else:
				print("There is no patient with that ID.")

		elif user_choice == 2:
			name = str(input("Enter the name of the patient: "))
			age = int(input("Enter in the age of the patient: "))
			gender = str(input("Enter in the gender of the patient: "))
			height = str(input("Enter in the height of the patient: "))
			weight = int(input("Enter in the weight of the patient in lbs: "))

			contact_list = {}
			print("You may optionally enter in patient contact numbers.")

			# Allow for users to enter in as many contacts as they desire with a null terminated loop.
			while True:
				contact = str(
					input("Please enter either label for this contact, or nothing to finish entering contacts: "))

				# Use string truthiness. If the contact is empty, break the loop. Otherwise, prompt for the number.
				if contact:
					number = str(input("Please enter the phone number associated with this label"))
					contact_list[contact] = number
				else:
					break

			# Create the new patient.
			Patient(name, age, gender, height, weight, contact_list)

		elif user_choice == 3:
			print("Before you quit we need to save a copy of the patients list.")
			file_name = str(input("Enter in the full path and file name without extension you would like to use: "))
			Patient.save_patients(file_name)
			break
		else:
			print("That number was not associated with any possible choice!")

	except ValueError:
		print("That is not a valid number!")

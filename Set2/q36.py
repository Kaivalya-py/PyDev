# Contact Book Application with Multiple Functionalities: Develop a contact book application in Python that enables users to add new contacts, display specific contact details, update contact details, delete a contact, list all contacts, and exit the application. Each contact should have a unique Contact ID, name, phone number, and email address. The program should use a dictionary to store contact details and provide a user-friendly menu for interaction.

def add_contact(contacts):
    contact_id = input("Enter Contact ID: ")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[contact_id] = [name, phone, email]
    print("Contact added successfully.")

def display_contact(contacts):
    contact_id = input("Enter Contact ID to display: ")
    if contact_id in contacts:
        print("Contact details:")
        print("Contact ID:", contact_id)
        print("Name:", contacts[contact_id][0])
        print("Phone:", contacts[contact_id][1])
        print("Email:", contacts[contact_id][2])
    else:
        print("Contact not found.")

def update_contact(contacts):
    contact_id = input("Enter Contact ID to update: ")
    if contact_id in contacts:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[contact_id] = [name, phone, email]
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    contact_id = input("Enter Contact ID to delete: ")
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def list_all_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for contact_id in contacts:
            print("Contact ID:", contact_id)
            print("Name:", contacts[contact_id][0])
            print("Phone:", contacts[contact_id][1])
            print("Email:", contacts[contact_id][2])
            print()

contacts = {}
while True:
    print("Menu:")
    print("1. Add contact")
    print("2. Display contact by ID")
    print("3. Update contact by ID")
    print("4. Delete contact by ID")
    print("5. List all contacts")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 6:
        break
    elif choice == 1:
        add_contact(contacts)
    elif choice == 2:
        display_contact(contacts)
    elif choice == 3:
        update_contact(contacts)
    elif choice == 4:
        delete_contact(contacts)
    elif choice == 5:
        list_all_contacts(contacts)
    else:
        print("Invalid choice")

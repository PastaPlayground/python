import sqlite3
import re

# python script for saving contacts
# info to save
# contact num
# name
# email address

# user functions
# add contact
# delete contact
# edit contact
# view contact list


# define connection and cursor
# create a db name contact book
connection = sqlite3.connect("contact_book.db")

cursor = connection.cursor()

# create contact table, each row represents 1 contact
create_table = """CREATE TABLE IF NOT EXISTS
contact(
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    number INT NOT NULL UNIQUE, 
    email TEXT NOT NULL UNIQUE) """

cursor.execute(create_table)


# add contact
def add_contact():

    contact_name = input("Your name: ")
    contact_num = int(input("Your phone number: "))

    # validate email with regex
    # email contains personal_info@domain
    contact_email = input("Your email: ")
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    while re.fullmatch(regex, contact_email):
        # INSERT VALUES into db
        cursor.execute(
            """INSERT INTO contact (name, number, email) VALUES (?, ?, ?)""",
            (contact_name, contact_num, contact_email),
        )
        connection.commit()
        print(
            f"New contact added successfully {contact_name} | {contact_num} | {contact_email}"
        )
    else:
        print("Invalid email format pls try again")
        add_contact()


# remove contact
def remove_contact():
    view_contact()

    contact_num = int(input("Enter contact number to delete: "))

    confirmation = input("Confirm delete? Y/N: ")
    if confirmation == "y":
        cursor.execute(
            "DELETE FROM contact WHERE number=:number ", {"number": contact_num}
        )
        connection.commit()
        print(f"Contact number {contact_num} deleted successfully")
    else:
        print("Contact not deleted")

    view_contact()


def clear_db():
    view_contact()
    confirmation = input("Confirm delete? Y/N: ")
    if confirmation == "y":
        cursor.execute("DELETE FROM contact")
        connection.commit()
        print(f"Contacts all deleted successfully")
    else:
        print("Contacts not deleted")


def view_contact():
    # VIEW CONTACT
    for row in cursor.execute("SELECT * FROM contact"):
        print(row)


def user_choice():
    print("Contact Book")
    actions = {1: "View", 2: "Add", 3: "Remove", 4: "Edit", 5: "Clear contacts"}
    for i, actions in actions.items():
        print(i, actions)

    userInput = int(input("What would you like to do?: "))
    if userInput == 1:
        view_contact()
    elif userInput == 2:
        add_contact()
    elif userInput == 3:
        remove_contact()

    elif userInput == 5:
        clear_db()


user_choice()

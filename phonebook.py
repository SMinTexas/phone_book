# You will write a command line program to manage a phone book. 
# When you start the phonebook.py program, it will print out a menu 
# and ask the user to enter a choice:

# $ python3 phonebook.py 
# Electronic Phone Book 
# ===================== 
# 1. Look up an entry 
# 2. Set an entry 
# 3. Delete an entry 
# 4. List all entries 
# 5. Quit
# What do you want to do (1-5)?

# 1. If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# 2. If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# 3. If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# 4. If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# 5. If they choose to quit, end the program.

phonebook_dict = {
    "Captain America": "111-222-3333",
    "Iron Man": "111-222-4444",
    "Thor": "111-222-5555",
    "Hulk": "111-222-6666",
    "Black Widow": "111-222-7777",
    "Hawkeye": "111-222-8888",
    "Thanos" : "505-050-5050"
}

def print_menu():
    print("Electronic Phone Book")
    print("=====================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

# Look up an existing phone number by name
def lookup_name(phone_book, search_str):
    for key, value in phone_book.items():
        if search_str in key:
            return value

# Set a new entry
def insert_name(phone_book, new_name, new_phone):
    phone_book[new_name] = new_phone

# Remove an existing entry
def delete_name(phone_book, name):
    del phone_book[name]

# Print all entries
def print_entries(phone_book):
    for key, value in phone_book.items():
        print(f'Found entry for {key}: {value}')

        def blank_line():
    print(" ")

def print_message(message, name, phone):
    print(f'{message} {name} {phone}')
    
# Main program 
print_menu()
user_choice = int(input("What do you want to do (1-5)? "))
blank_line()

if user_choice == 1:
    name = input("Name: ")
    phone = lookup_name(phonebook_dict, name)
    print_message('Found entry for', name, phone)
    blank_line()
    #print_menu()
elif user_choice == 2:
    name = input("Name: ")
    phone = input("Phone Number: ")
    insert_name(phonebook_dict, name, phone)
    print_message('Entry stored for', name, "")
    blank_line
    #print_menu()
elif user_choice == 3:
    name = input("Name: ")
    delete_name(phonebook_dict, name)
    print_message('Deleted entry for', name, "")
    blank_line()
    #print_menu()
elif user_choice == 4:
    print_entries(phonebook_dict)
    blank_line()
    #print_menu()
else:
    print("Bye")

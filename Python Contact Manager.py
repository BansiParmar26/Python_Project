def add_contact(contact_book):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contact_book[name] = phone
    print(f"Contact for {name} added successfully!")

def view_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        print("\nContacts List:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")

def search_contact(contact_book):
    name = input("Enter the name to search: ")
    if name in contact_book:
        print(f"{name}: {contact_book[name]}")
    else:
        print(f"Contact for {name} not found.")

def main():
    contact_book = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contacts(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            print("Exiting the contact book...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact with name '{name}' already exists. Please choose a different name.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for name, details in self.contacts.items():
                print(f"{name}: {details['phone_number']} | {details['email']} | {details['address']}")

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details['phone_number']:
                results.append((name, details))
        return results

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact with name '{name}' not found. Unable to update.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact with name '{name}' not found. Unable to delete.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nCONTACT BOOK MENU:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search Results:")
                for name, details in results:
                    print(f"{name}: {details['phone_number']} | {details['email']} | {details['address']}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone_number, email, address)
        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

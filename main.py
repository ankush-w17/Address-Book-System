class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, number, email):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.number=number
        self.email=email




class AddressBook:
    def __init__(self,name):
        self.name=name
        self.contact_list=[]


    def is_duplicate(self, first_name): 
        for contact in self.contact_list:
            if contact.first_name.lower() == first_name.lower():
                return True
        return False

    def add_contact(self):
            first=input("First Name: ")
            if self.is_duplicate(first):
                print(f"Error: Contact '{first}' already exists in this address book!")
                return
            last=input("Last Name: ")
            address=input("Address: ")
            city=input("City: ")
            state=input("State: ")
            zip=input("Zip: ")
            number=input("Phone Number: ")
            email=input("Email: ")

            newContact=Contact(first,last,address,city,state,zip,number,email)
            self.contact_list.append(newContact)

    def edit_contact(self):
        name=input("Enter First Name of contact to be edited: ")
        for contact in self.contact_list:
            if(contact.first_name==name):
                print("Re-enter the details for ",name)
                contact.first_name=input("First Name: ")
                contact.last_name=input("Last Name: ")  
                contact.address=input("Address: ")
                contact.city=input("City: ")
                contact.state=input("State: ")
                contact.zip=input("Zip: ")
                contact.number=input("Phone Number: ")
                contact.email=input("Email: ")

    def delete_contact(self):
        name=input("Enter the name of contact to be deleted :")
        for contact in self.contact_list:
            if(contact.first_name==name):
                self.contact_list.remove(contact)
                print("Contact deleted Successfully")


    def add_multiple(self):
        n= int(input("Enter the number of people to be added :"))
        for i in range(n):
            print("Enter details")
            self.add_contact()


class AddressBookSystem:
    def __init__(self):
        self.addressBookDict = {}
    
    def create_address_book(self):
        name = input("Enter the name of the address book: ")
        
        if name in self.addressBookDict:
            print(f"Error: Address book '{name}' already exists!")
            return None
        
        new_book = AddressBook(name)
        self.addressBookDict[name] = new_book
        print(f"Address book '{name}' created successfully!\n")
        return new_book

    def select_address_book(self):
        if not self.addressBookDict:
            print("\nNo address books available. Please create one first.")
            return None
        
        print("\nAvailable Address Books")
        for name in self.addressBookDict.keys():
            print(f"- {name}")
        
        book_name = input("\nEnter the name of the address book: ")
        
        if book_name in self.addressBookDict:
            print(f"Selected '{book_name}'.\n")
            return self.addressBookDict[book_name]
        else:
            print(f"Address book '{book_name}' not found.")
            return None

    def display_all_books(self):
        if not self.addressBookDict:
            print("\nNo address books in the system.")
        else:
            print("\nAll Address Books")
            for name, book in self.addressBookDict.items():
                print(f"- {name} ({len(book.contact_list)} contacts)")
            print()

    def search_person_by_city(self, city):
        results = []
        for book_name, book in self.addressBookDict.items():
            for contact in book.contact_list:
                if contact.city.lower() == city.lower():
                    results.append((book_name, contact))
        return results

    def search_person_by_state(self, state):
        results = []
        for book_name, book in self.addressBookDict.items():
            for contact in book.contact_list:
                if contact.state.lower() == state.lower():
                    results.append((book_name, contact))
        return results

    def get_count_by_city(self):
        city_count = {}
        
        for book in self.addressBookDict.values():
            for contact in book.contact_list:
                city = contact.city
                if city in city_count:
                    city_count[city] += 1
                else:
                    city_count[city] = 1
        
        return city_count

    def get_count_by_state(self):
        state_count = {}
        
        for book in self.addressBookDict.values():
            for contact in book.contact_list:
                state = contact.state
                if state in state_count:
                    state_count[state] += 1
                else:
                    state_count[state] = 1
        
        return state_count

    def display_count_by_city_or_state(self):
        print("\n--- View Count ---")
        print("1. Count by City")
        print("2. Count by State")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city_count = self.get_count_by_city()
            
            if not city_count:
                print("\nNo contacts available in any address book.")
            else:
                print("\n--- Count by City ---")
                for city, count in city_count.items():
                    print(f"{city}: {count} person(s)")
                print(f"\nTotal cities: {len(city_count)}")
        
        elif choice == "2":
            state_count = self.get_count_by_state()
            
            if not state_count:
                print("\nNo contacts available in any address book.")
            else:
                print("\n--- Count by State ---")
                for state, count in state_count.items():
                    print(f"{state}: {count} person(s)")
                print(f"\nTotal states: {len(state_count)}")
        
        else:
            print("Invalid choice!")

    def search_by_city_or_state(self):
        print("\n--- Search Person ---")
        print("1. Search by City")
        print("2. Search by State")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city = input("Enter city name: ")
            results = self.search_person_by_city(city)
            
            if not results:
                print(f"\nNo persons found in city '{city}'.")
            else:
                print(f"\nPersons in {city}")
                for book_name, contact in results:
                    print(f"\nAddress Book: {book_name}")
                    print(contact.first_name)
                print(f"\nTotal: {len(results)} person(s) found")
        
        elif choice == "2":
            state = input("Enter state name: ")
            results = self.search_person_by_state(state)
            
            if not results:
                print(f"\nNo persons found in state '{state}'.")
            else:
                print(f"\nPersons in {state} ")
                for book_name, contact in results:
                    print(f"\nAddress Book: {book_name}")
                    print(contact.first_name)
                print(f"\nTotal: {len(results)} person(s) found")
        
        else:
            print("Invalid choice!")




def main():
    print("Welcome to Address Book System")
    obj=AddressBookSystem()
    current_book=None
    while True:
        print("1. Create New Address Book")
        print("2. Select Address Book")
        print("3. Display All Address Books")
        print("4. Search Person by City or State") 
        print("5. View Count by City or State")  
        print("6. Exit")

        if current_book:
            print(f"\nCurrently working with: '{current_book.name}'")
            print("7. Add Contact")
            print("8. Add Multiple Contacts")
            print("9. Edit Contact")
            print("10. Delete Contact")


        choice=input("\nEnter your Choice :")

        if choice == "1":
            new_book = obj.create_address_book()  
            if new_book:
                current_book = new_book 
            
        elif choice == "2":
            current_book = obj.select_address_book()
            
        elif choice == "3":
            obj.display_all_books()
            
        elif choice == "4":
            obj.search_by_city_or_state()  
            
        elif choice == "5":
            obj.display_count_by_city_or_state() 
            
        elif choice == "6":
            print("\nThank you for using Address Book System!")
            break
            
        elif choice == "7" and current_book:
            current_book.add_contact()
            
        elif choice == "8" and current_book:
            current_book.add_multiple()
            
        elif choice == "9" and current_book:
            current_book.edit_contact()
            
        elif choice == "10" and current_book:
            current_book.delete_contact()

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
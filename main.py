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

    def add_contact(self):
            first=input("First Name: ")
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


def main():
    print("Welcome to Address Book System")
    obj=AddressBookSystem()
    current_book=None
    while True:
        print("1. Create New Address Book")
        print("2. Select Address Book")
        print("3. Display All Address Books")
        print("4. Exit")

        if current_book:
            print(f"\nCurrently working with: '{current_book.name}'")
            print("5. Add Contact")
            print("6. Add Multiple Contacts")
            print("7. Edit Contact")
            print("8. Delete Contact")


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
            print("\nThank you for using Address Book System")
            break
            
        elif choice == "5" and current_book:
            current_book.add_contact()
            
        elif choice == "6" and current_book:
            current_book.add_multiple()
            
        elif choice == "7" and current_book:
            current_book.edit_contact()
            
        elif choice == "8" and current_book:
            current_book.delete_contact()

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
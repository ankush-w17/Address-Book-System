contact_list=[]
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

ankush=Contact("Ankush","Wadhwani","A-35","Bareilly","Uttar Pradesh","243001","8791859640","ankushwadhwani222@gmail.com")
print(ankush.email)


class AdressBook:
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
            contact_list.append(newContact)

    def edit_contact(self):
        name=input("Enter First Name of contact to be edited: ")
        for contact in contact_list:
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
        for contact in contact_list:
            if(contact.first_name==name):
                contact_list.remove(contact)
                print("Contact deleted Successfully")


    def add_multiple(self):
        n= int(input("Enter the number of people to be added :"))
        for i in range(n):
            print("Enter details")
            self.add_contact()




book=AdressBook()
book.add_multiple()
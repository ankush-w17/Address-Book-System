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
    def add_contact():
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

AdressBook.add_contact()
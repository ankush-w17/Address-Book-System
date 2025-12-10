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

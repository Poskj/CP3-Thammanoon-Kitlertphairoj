class Customer:
    name = ""
    lastName = ""
    phone = ""

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")
        print("Phone :",self.phone)

customer1 = Customer()
customer1.name = "Thammanoon"
customer1.lastName = "Kitlertphairoj"
customer1.phone = "4904810350453"
customer1.addCart()

customer2 = Customer()
customer2.name = "Teethat"
customer2.lastName = "Lhaosukskul"
customer2.phone = "4904810811886"
customer2.addCart()

customer3 = Customer()
customer3.name = "Thanapol"
customer3.lastName = "Wong-asa"
customer3.phone = "4904810470571"
customer3.addCart()

customer4 = Customer()
customer4.name = "Thanakorn"
customer4.lastName = "Changchengpanich"
customer4.phone = "4904810470571"
customer4.addCart()
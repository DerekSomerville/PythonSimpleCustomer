from src.Customers import Customers
class LogIn:
    def get_password(self,email_address):
        customers = Customers()
        customer_data = customers.load_customers()
        password = ""
        counter = 0
        while password == "" and counter < len(customer_data):
            if email_address == customer_data[counter][0]:
                password = customer_data[counter][3]
            counter += 1
        return password

    def log_in(self):
        email_address = input("Enter your email address")
        password = self.get_password(email_address)
        if password == "":
            print("You are not a user")
        else:
            if input("Enter password") == password:
                print("You are logged in")
            else:
                print("Wrong password, no second chances")

class Customer:
    def __init__(self, name, father_name, customer_id, balance):
        self.name = name
        self.father_name = father_name
        self.customer_id = customer_id
        self.balance = balance
        
    def __str__(self):
        return f"Name: {self.name}, Father name: {self.father_name}, Customer ID: {self.customer_id}, Balance: {self.balance}"
    

list_customers = []    

def add_customer():
    while True :
        customer_id = input("Enter your Customer ID: ")
        if any(customer.customer_id == customer_id for customer in list_customers):
            print("This ID is already exists.Please enter a uinque one.")
        else : 
            new_name = input("Enter your name: ")
            new_father_name = input("Enter your father's name: ")
            try:
                balance = float(input("Enter you initial balance without any marks like $: "))
            except ValueError :
                print("Invalid balance input.Try again.")
                return
            
        new_customer = Customer(new_name, new_father_name, customer_id, balance)
        list_customers.append(new_customer)
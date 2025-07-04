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
                balance = float(input("Enter your initial balance without any marks like $: "))
            except ValueError :
                print("Invalid balance input.Try again.")
                return
            
        new_customer = Customer(new_name, new_father_name, customer_id, balance)
        list_customers.append(new_customer)
        
def find_customer():
    customer_id = input("Enter yor ID: ")
    for customer in list_customers :
        if customer.customer_id == customer_id:
            print("Customer found: ")
            print(customer)
            return
    print("Customer not found.")
    
def show_customers():
    if not list_customers:
        print("No Customer available.")
    else:
        for customer in list_customers:
            print("List Customers: ")
            print(customer)
            
def edit_customer():
    customer_id = input("Enter yor ID: ")
    for customer in list_customers:
        if customer.customer_id == customer_id :
            print("Customer found: ")
            new_name = input("Enter your new name: ")
            customer.name = new_name
            print("Name updated successfully.")
            try:
                new_balance = float(input("Enter your new initial balance without any marks like $: "))
            except ValueError :
                print("Invalid balance input.Try again.")
                return
            customer.balance = new_balance
            print("Initial balance updated successfully.")
            return
    print("Customer not found.")
    
def delete_customer():
        customer_id = input("Enter yor ID: ")
        for customer in list_customers:  
            if customer.customer_id == customer_id :
                list_customers.remove(customer)
                print("Customer deleted.")
            return
        print("Customer not found.") 

def request_loan():
        customer_id = input("Enter yor ID: ")
        for customer in list_customers:  
            if customer.customer_id == customer_id :
                try:
                    amount = float(input("Enter the amount of loan without any marks like $: "))
                except ValueError :
                    print("Invalid amount.")
                    return
                
                if amount <= customer.balance :
                    customer.balance += amount
                    print(f"Loan approved! New balance: {customer.balance}")
                else : 
                    print("Loan amount exceeds balance.")
                    return
        print("Customer not found.")
                    
                    
        
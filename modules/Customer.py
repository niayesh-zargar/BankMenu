class Customer:
    def __init__(self, name, father_name, customer_id, balance):
        self.name = name
        self.father_name = father_name
        self.customer_id = customer_id
        self.balance = balance
        
    def __str__(self):
        return f"Name: {self.name}, Father name: {self.father_name}, Customer ID: {self.customer_id}, Balance: {self.balance}"
    
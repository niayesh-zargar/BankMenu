class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    def __str__(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}"
    

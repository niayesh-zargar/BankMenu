class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
    def __str__(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}"
    
list_employees = []

def add_employee():
    while True :
        employee_id = input("Enter employee ID: ")
        if any(employee.employee_id == employee_id for employee in list_employees) :
            print("This ID already exists. Please enter a unique one.")
        else :
            break 
        
    name = input("Enter employee name: ")
    try : 
        salary = float(input("Enter your salary: "))
    except ValueError : 
        print("Invalid balance input.")
        return
    
    new_employee = Employee(name , employee_id , salary)
    list_employees.append(new_employee)
    print("employee added successfully.") 
    
def find_employee():
    eid = input("Enter employee ID: ")
    for employee in list_employees :
        if employee.employee_id == eid :
            print("Employee found: ")
            print(employee)
            return
    print("Employee not found.")
    
def show_employees():
    if not list_employees :
        print("No employees available.")
    else :
        for employee in list_employees :
            print(employee)

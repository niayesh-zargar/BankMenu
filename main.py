from modules.Customer import *
from modules.Employee import *

while True :
    print('\n------ Bank Menu ------\n')
    print('1. Add New Customer ')
    print('2. Show All Customers ')
    print('3. Search Customer (By ID) ')
    print('4. Edit Customer Info (By ID) ')
    print('5. Delete Customer (By ID) ')
    print('6. Reaquest Loan (By ID) ')
    print('7. Add Employee ')
    print('8. Show All Employees ')
    print('9. Search Employee (By ID) ')
    print('10. Edit Employee Info (By ID) ')
    print('11. Delete Employee (By ID) ')
    print('12. Exit')
    print("-----------------------")
    choice = input('Enter the number of your option: ')
    
    try :
        choice = int(choice)
        if choice == 1 : add_customer()
        elif choice == 2 : show_customers()
        elif choice == 3 : find_customer()
        elif choice == 4 : edit_customer()
        elif choice == 5 : delete_customer()
        elif choice == 6 : request_loan()
        elif choice == 7 : add_employee()
        elif choice == 8 : show_employees()
        elif choice == 9 : find_employee()
        elif choice == 10 : edit_employee()
        elif choice == 11 : delete_employee()
        elif choice == 12 : 
            break
    
    except ValueError : 
        print('It\'s an invalid value try again!') 

    

# Project Structure Explanation

This project follows a modular approach for better organization and scalability. The structure of the project is as follows:

## 1. Project Folder Layout:
- **Main File (`main.py`)**:  
  This is the entry point for the program, placed outside the "Modules" folder. It handles the execution of the program and contains the main menu, where the user interacts with the system.
- **Modules Folder**:  
  Inside the "Modules" folder, there are two separate files:
    - **`customer.py`**: Contains the `Customer` class and its associated functions (e.g., add, edit, delete, search customers).
    - **`employee.py`**: Contains the `Employee` class and its related functions (e.g., add, edit, delete, search employees).

## 2. Modular Approach:  
- By separating the **Customer** and **Employee** classes into different modules, we keep each class's functionality independent, making the code more maintainable and scalable.
- The **`main.py`** file serves as the central hub where both **Customer** and **Employee** modules are imported. It provides a user interface with a simple menu for performing actions like adding, searching, editing, and deleting customers and employees.

## 3. Why This Structure?
- **Separation of Concerns**: Each module (Customer and Employee) is responsible for its specific set of operations. This keeps the code clean and makes future changes easier to manage.
- **Scalability**: As the project grows, you can easily add more modules (e.g., for handling loans, transactions, etc.) without affecting the existing structure.
- **Maintainability**: By isolating classes and their corresponding methods, future developers can easily understand the purpose of each module and make necessary changes without affecting others.

## 4. Project Workflow:
- The **Customer** and **Employee** classes are defined in their respective files inside the **Modules** folder.
- **`main.py`** imports the functions from these modules to handle user interactions. Based on user input, it calls the appropriate functions (e.g., adding a customer, listing employees, etc.).
- The modular design allows easy maintenance and future development, as each file is dedicated to a specific functionality.

---

### **Folder Structure in Detail**:

```
bank_project/
│
├── main.py              👈 Main program entry point
│
└── Modules/             👈 Folder containing Customer and Employee modules
    ├── customer.py      👈 Contains Customer class and functions
    └── employee.py      👈 Contains Employee class and functions
```

---

### **Conclusion**

The project is designed with modularity in mind, ensuring that each class and its functionality are neatly organized. By separating the code into different modules, the project becomes easier to maintain, extend, and scale. The **`main.py`** file serves as the central point where all functionality is brought together and executed based on user input.

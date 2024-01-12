from DatabaseConnector import connect_to_database
from Customer import Customer



def customer_management():
    print("welcome to Customer Management Services")
    print()

    print("1. Add Customer")
    print("2. Read Customer")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. Exit")
    print()
    user_input = input("enter your value: ")
    print()
    customer = Customer(None, None, None, None, None, None, None)
    if user_input == "1":
        print()
        customer_id = input("enter Customer ID: ")
        customer_name = input("Enter Customer Name: ")
        customer_email = input("Enter Customer Email: ")
        customer_address = input("Enter Customer Address: ")
        customer_date_of_birth = input("Enter Customer Date of Birth: ")
        customer_phone = input("Enter Customer Phone: ")
        customer_gender = input("Enter Customer Gender: ")

        customer.add(connect_to_database(), "Customer", customer_id,
                     customer_name, customer_email, customer_address,
                     customer_phone, customer_date_of_birth, customer_gender)
    elif user_input == "2":
        print()
        customer.read(connect_to_database())
    elif user_input == "3":
        print()
        customer_id = input("enter Customer ID: ")
        print("Selected customer details")
        customer.selected_customer(connect_to_database(), customer_id)
        column_name = input("which column you want to change please enter correctly: ")
        new_value = input("new value: ")
        customer.update(connect_to_database(), "customer", customer_id, column_name, new_value)
    elif user_input == "4":
        print()
        customer_id = input("enter Customer ID: ")
        customer.delete(connect_to_database(), "customer", customer_id)
    elif user_input == "5":
        print()
        print("Exiting Customer Management Services. Goodbye!")

    else:
        print()
        print("Invalid input. Please enter a number between 1 and 5.")


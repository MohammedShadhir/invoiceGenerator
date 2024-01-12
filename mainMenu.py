from Management.CustomerMangement import customer_management
from Management.InvoiceMangement import invoice_generator
from Management.ProductManagement import product_management


def Menu():
    try:
        print()
        print("welcome to the invoice generator")
        print("what type of service you are looking for choose an option")
        print()
        print("1. Customer Management")
        print("2. Product Management")
        print("3. generate Invoice")
        print()
        user_input = input("enter your value: ")

        if user_input == "1":
            print()
            customer_management()
        elif user_input == "2":
            print()
            product_management()
        elif user_input == "3":
            print()
            invoice_generator()
        else:
            print()
            print("please select services")
    except Exception as e:
        print("Error:", e)
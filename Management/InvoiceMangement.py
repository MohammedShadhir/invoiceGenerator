from DatabaseConnector import connect_to_database
from Invoice import Invoice


def invoice_generator():
    print("welcome to Generate Invoice")
    print()

    print("1. Generate Invoice")
    print("2. Read Invoice")
    print("3. Update Invoice")
    print("4. Delete Invoice")
    print("5. Exit")
    print()

    invoice = Invoice(None, None, None,
                      None, None, None,
                      None, None)
    user_input = input("enter your value: ")
    print()
    if user_input == "1":
        print()
        invoice_number = input("enter invoice number: ")
        invoice_date = input("enter invoice date: ")
        customer_name = input("enter customer name: ")
        product_names = input("enter product name: ")
        units_per_product = input("enter units per product: ")
        units_price_per_product = input("enter units prices per product: ")
        total_price_per_product = input("enter total prices per product: ")
        discount = input("enter discount: ")

        invoice.add_invoice(connect_to_database(), invoice_number, invoice_date, customer_name, product_names,
                            units_per_product, units_price_per_product, total_price_per_product, discount)

    elif user_input == "2":
        print()
        invoice.read(connect_to_database())
    elif user_input == "3":
        print()
        invoice_number = input("enter invoice number: ")
        print("Selected invoice details")
        invoice.selected_invoice(connect_to_database(), invoice_number)
        column_name = input("which column you want to change please enter correctly: ")
        new_value = input("new value: ")
        invoice.update(connect_to_database(), "invoice", invoice_number, column_name, new_value)
    elif user_input == "4":
        print()
        invoice_number = input("enter invoice number: ")
        invoice.delete(connect_to_database(), "invoice", invoice_number)
    elif user_input == "5":
        print()
        print("Exiting Customer Management Services. Goodbye!")
    else:
        print()
        print("Invalid input. Please enter a number between 1 and 5.")



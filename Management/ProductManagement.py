from DatabaseConnector import connect_to_database
from Product import Product


def product_management():
    print("Product Management Services")
    print("_______________________")

    print("1. Add Product")
    print("2. Read Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    print()

    user_input = input("enter your value: ")
    product = Product(None, None, None, None, None, None)
    if user_input == "1":
        product_id = input("enter product id: ")
        product_name = input("enter product name: ")
        product_description = input("enter product description: ")
        product_purchase_price = input("enter product purchase price: ")
        product_selling_price = input("enter product selling price: ")
        product_quantity = input("enter product quantity: ")

        product.add_product(connect_to_database(),product_id, product_name, product_description,
                            product_purchase_price, product_selling_price, product_quantity)

    elif user_input == "2":
        product.read(connect_to_database())
    elif user_input == "3":
        product_id = input("enter product id: ")
        print("Selected product details")
        product.selected_product(connect_to_database(), product_id)
        column_name = input("which column you want to change please enter correctly: ")
        new_value = input("new value: ")
        product.update(connect_to_database(), product_id, column_name, new_value)
    elif user_input == "4":
        product_id = input("enter product id: ")
        product.delete(connect_to_database(), product_id)
    elif user_input == "5":
        print("Exiting Customer Management Services. Goodbye!")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")


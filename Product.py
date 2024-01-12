import mysql
from prettytable import prettytable


class Product:
    def __init__(self, product_id, product_name, description, purchase_price, selling_price, quantity):
        self.productId = product_id
        self.productName = product_name
        self.description = description
        self.purchasePrice = purchase_price
        self.sellingPrice = selling_price
        self.quantity = quantity

    @staticmethod
    def read(connection):
        try:
            query = "SELECT * FROM Product"
            cursor = connection.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            table = prettytable.PrettyTable(columns)
            print()
            for row in cursor.fetchall():
                table.add_row(row)
            print(table)

            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def add_product(connection, product_id, product_name, description, purchase_price, selling_price, quantity):
        query = "INSERT INTO Product (productId, productName, description, purchasePrice, sellingPrice, quantity) VALUES (%s, %s, %s, %s, %s, %s)"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (product_id, product_name, description, purchase_price, selling_price, quantity))
            connection.commit()
            print()
            print("Product inserted successfully.")
            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def delete(connection,product_id):
        query = "DELETE FROM Product WHERE productId = %s"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (product_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("Row deleted successfully.")
            else:
                print("No row found with product ID", product_id)

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def update(connection, product_id, column_name, new_value):
        query = f"UPDATE Product SET {column_name} = %s WHERE productId = %s"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (new_value, product_id))
            connection.commit()

            if cursor.rowcount > 0:
                print("Data updated successfully.")
            else:
                print(f"Failed to update data. Product with ID {product_id} not found.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def selected_product(connection, product_id):
        try:
            query = "SELECT * FROM product where productId = %s"
            cursor = connection.cursor()
            print("Connection Established successfully")
            cursor.execute(query, (product_id,))
            columns = [column[0] for column in cursor.description]

            # Create a PrettyTable object
            table = prettytable.PrettyTable(columns)

            for row in cursor.fetchall():
                # Add each row to the table
                table.add_row(row)

            # Set the alignment of the columns
            table.align = "l"

            # Print the table
            print(table)

            cursor.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)



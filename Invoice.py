import sqlite3

import mysql
from prettytable import prettytable


class Invoice:
    def __init__(self, invoice_number, invoice_date, customer_name, product_names, units_per_product, unit_price_per_product, total_price_per_product, discount):
        self.invoiceNumber = invoice_number
        self.invoiceDate = invoice_date
        self.customerName = customer_name
        self.productNames = product_names
        self.unitsPerProduct = units_per_product
        self.unitPricePerProduct = unit_price_per_product
        self.totalPricePerProduct = total_price_per_product
        self.discount = discount

    @staticmethod
    def read(connection):
        try:
            query = "SELECT * FROM Invoice"
            print("Connection Established successfully")
            cursor = connection.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]

            table = prettytable.PrettyTable(columns)

            for row in cursor.fetchall():
                table.add_row(row)
            table.align = "l"
            print(table)

            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def add_invoice(connection, invoice_number, invoice_date, customer_name, product_names, units_per_product, unit_price_per_product, total_price_per_product, discount):
        query = f"INSERT INTO Invoice (invoiceNumber, invoiceDate, customerName, productNames, unitsPerProduct, unitPricePerProduct, totalPricePerProduct, discount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (invoice_number, invoice_date, customer_name, product_names, units_per_product, unit_price_per_product, total_price_per_product, discount))
            connection.commit()

            print("Invoice inserted successfully.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def delete(connection, table_name, invoice_number):
        query = f"DELETE FROM {table_name} WHERE invoiceNumber = %s"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (invoice_number,))
            connection.commit()

            if cursor.rowcount > 0:
                print("Row deleted successfully.")
            else:
                print(f"No row found with invoice number {invoice_number}.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def update(connection, table_name, invoice_number, column_name, new_value):
        query = f"UPDATE {table_name} SET {column_name} = %s WHERE invoiceNumber = %s"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (new_value, invoice_number))
            connection.commit()

            if cursor.rowcount > 0:
                print("Data updated successfully.")
            else:
                print(f"Failed to update data. Invoice with ID {invoice_number} not found.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def selected_invoice(connection, invoice_number):
        try:
            query = "SELECT * FROM Invoice WHERE invoiceNumber = %s"
            cursor = connection.cursor()
            cursor.execute(query, (invoice_number,))
            columns = [column[0] for column in cursor.description]
            # Create a PrettyTable object
            table = prettytable.PrettyTable(columns)
            for row in cursor.fetchall():
                table.add_row(row)
            # Set the alignment of the columns
            table.align = "l"
            # Print the table
            print(table)
            cursor.close()
        except mysql.connector.Error as e:
            print(e)

import mysql
from prettytable import prettytable

from DatabaseConnector import connect_to_database


class Customer:
    def __init__(self, customer_id, customer_name, email, address, contact_number, date_of_birth, gender):
        self.customerId = customer_id
        self.customerName = customer_name
        self.email = email
        self.address = address
        self.contactNumber = contact_number
        self.dateOfBirth = date_of_birth
        self.gender = gender

    @staticmethod
    def read(connection):
        try:
            query = "SELECT * FROM customer"
            cursor = connection.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            table = prettytable.PrettyTable(columns)

            for row in cursor.fetchall():
                table.add_row(row)
            table.align = "l"

            # Print the table
            print(table)
            cursor.close()
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def add(connection, table_name, customer_id, customer_name, email, address, contact_number, date_of_birth, gender):
        query = f"INSERT INTO {table_name} (customerId, customerName, email, address, contactNumber, dateOfBirth, gender) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (customer_id, customer_name, email, address, contact_number, date_of_birth, gender))
            connection.commit()
            print()
            print("Data inserted successfully.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def update(connection, table_name, customer_id, column_name, new_value):
        query = f"UPDATE {table_name} SET {column_name} = %s WHERE customerId = %s"

        try:
            cursor = connection.cursor()
            cursor.execute(query, (new_value, customer_id))
            connection.commit()

            if cursor.rowcount > 0:
                print("Data updated successfully.")
            else:
                print(f"Failed to update data. Customer with ID {customer_id} not found.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def delete(connection, table_name, customer_id):
        query = f"DELETE FROM {table_name} WHERE customerId = %s"


        try:

            cursor = connection.cursor()
            cursor.execute(query, (customer_id,))
            connection.commit()

            if cursor.rowcount > 0:
                print("Row deleted successfully.")
            else:
                print(f"No row found with customer ID {customer_id}.")

            cursor.close()
            connection.close()
            print("Connection Closed....")
        except mysql.connector.Error as e:
            print(e)

    @staticmethod
    def selected_customer(connection, customer_id):
        try:
            query = "SELECT * FROM customer WHERE customerId = %s"
            cursor = connection.cursor()
            cursor.execute(query, (customer_id,))
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
        except mysql.connector.Error as e:
            print(e)
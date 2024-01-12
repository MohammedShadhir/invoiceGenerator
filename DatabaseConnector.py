import mysql.connector
from mysql.connector import Error


def connect_to_database():
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", password="shadhir12300",
                                      database="invoiceGenerator")

        if cnx.is_connected():
            return cnx
            # db_Info = cnx.get_server_info()
            # print("Connect to MySql Server successfully", db_Info)
            # cursor = cnx.cursor()
            # cursor.execute("select database();")
            # records = cursor.fetchone()
            # print("connect to database", records)
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

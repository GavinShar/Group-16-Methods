import mysql.connector
import sys

class user_info:

        ## Connects to the database
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="") ## Needs Database name
        print("Successful connection.")

    except:
        print("Failed connection.")


    def order_history_add (self):

        query = "INSERT INTO history (id, transacDate, userID, ISBN) Values (%s, %s, %s, %s)"
        data = id, "6/9/6969", userID, isbn
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()

    def order_history_view (self):

        query = "SELECT * FROM history"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def user_login(self):

        query = "SELECT userID"
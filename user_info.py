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


    def order_history_add (self, id, transacDate, user_id, isbn):

        query = "INSERT INTO history (id, transacDate, userID, ISBN) Values (%s, %s, %s, %s)"
        data = id, transacDate, user_id, isbn
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()

    def order_history_view (self):

        query = "SELECT * FROM history"
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        connection.commit()

    def user_login(self, userID):

        query = "SELECT userPass FROM user_info WHERE userID = %s"
        cursor = connection.cursor()
        cursor.execute(query, userID)
        result = cursor.fetchall()

        if (result != userPass):
            print ("Invalid Password")

    def edit_login(self, userID, userPass):

        query = "UPDATE user_info SET userPass = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, userPass, userID)
        connection.commit()

    def edit_payment (self, userID, cardNum, cardExp, cardCVV):

        query = "UPDATE user_info SET cardNum = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, cardNum, userID)
        connection.commit()
        query = "UPDATE user_info SET cardExp = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, cardExp, userID)
        connection.commit()
        query = "UPDATE user_info SET cardCVV = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, cardCVV, userID)
        connection.commit()

    def edit_shipping(self, userID, address, city, state, zip):

        query = "UPDATE user_info SET address = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, address, userID)
        connection.commit()
        query = "UPDATE user_info SET city = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, city, userID)
        connection.commit()
        query = "UPDATE user_info SET cardNum = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, state, userID)
        connection.commit()
        query = "UPDATE user_info SET zip = '%s' WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, zip, userID)
        connection.commit()

    def delete_account (self, userID):

        query = "DELETE FROM user_info WHERE userID = '%s'"
        cursor = connection.cursor()
        cursor.execute(query, userID)
        connection.commit()

    def create_user (self, userID, userPass, cardNum, cardExp, cardCVV, address, city, state, zip):

        query = "INSERT INTO user_info (userID, userPass, cardNum, cardExp, cardCVV, address, city, state, zip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(query, userID, userPass, cardNum, cardExp, cardCVV, address, city, state, zip)
        connection.commit()
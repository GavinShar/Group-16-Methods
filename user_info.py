import mysql.connector
import sys
from history import History

class user_info:

#    def order_history_add (self, id, transacDate, user_id, isbn):

#        query = "INSERT INTO history (id, transacDate, userID, ISBN) Values (%s, %s, %s, %s)"
#        data = id, transacDate, user_id, isbn
#        cursor = connection.cursor()
#        cursor.execute(query, data)
#        connection.commit()

#    def order_history_view (self):

#        query = "SELECT * FROM history"
#        cursor = connection.cursor()
#        cursor.execute(query)
#        result = cursor.fetchall()

#        connection.commit()

    def user_login(connection, cursor, userID, userPass):

        query = "SELECT userPass FROM user_info WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if (result[0][0] != userPass):
            print ("Invalid Password")
            return True
        return False

    def edit_login(connection, cursor, userID, userPass):

        query = "UPDATE user_info SET userPass = '"+userPass+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def edit_payment (connection, cursor, userID, cardNum, cardExp, cardCVV):

        query = "UPDATE user_info SET cardNum = '"+cardNum+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query = "UPDATE user_info SET cardExp = '"+cardExp+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query = "UPDATE user_info SET cardCVV = '"+cardCVV+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def edit_shipping(connection, cursor, userID, address, city, state, zip):

        query = "UPDATE user_info SET address = '"+address+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query = "UPDATE user_info SET city = '"+city+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query = "UPDATE user_info SET cardNum = '"+state+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        query = "UPDATE user_info SET zip = '"+zip+"' WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def delete_account (connection, cursor, userID):

        cursor.execute("DELETE FROM cart WHERE userID='" + userID + "'")
        connection.commit()
        History.clearHistory(connection, cursor, userID)
        query = "DELETE FROM user_info WHERE userID = '"+userID+"'"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

    def create_user (connection, cursor, userID, userPass, cardNum, cardExp, cardCVV, address, city, state, zip):

        query = "INSERT INTO user_info (userID, userPass, cardNum, cardExp, cardCVV, address, city, state, zip) VALUES ('"+userID+"', '"+userPass+"', '"+cardNum+"', '"+cardExp+"', "+cardCVV+", '"+address+"', '"+city+"', '"+state+"', '"+zip+"')"
        #cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
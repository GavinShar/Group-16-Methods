from datetime import date
import mysql.connector
import sys
import random

class History:
    def addTransac(theConnection, theCursor, user_id, ISBN):
        #creates an infinite loop that is broken when the transaction is added to the database
        while True:
            #the transaction id is just a randomly generated integer
            transac_id = random.randint(1, 1000)

            #creates a select query to check if the random id already exists in the database
            myString = ("SELECT id FROM history WHERE id = " + str(transac_id))
            theCursor.execute(myString)
            result = theCursor.fetchall()

            #the transaction is added to the database if the id is not already in the database, else a new id is generated
            if result == []:
                myString = ("INSERT INTO history (id, transacDate, userID, ISBN) VALUES (" + str(transac_id) + ", " + str(date.today()) + ", '" + user_id + "', '" + ISBN + "')")
                theCursor.execute(myString)
                theConnection.commit()
                #verification of insertion for testing purposes
                #print(theCursor.rowcount, "record inserted")
                break


    def viewHistory(theConnection, theCursor, user_id):
        #runs a query that grabs every ISBN purchased by the user and the date purchased; the results are printed to the screen
        myString = ("SELECT transacDate, ISBN FROM history WHERE userID = '" + user_id + "'")
        theCursor.execute(myString)
        result = theCursor.fetchall()
        for x in result:
            print("Date:", x[0], "ISBN:", x[1])

    #NOTE: THIS FUNCTION IS ONLY TO BE USED WHEN A USER IS DELETING THEIR ACCOUNT
    def clearHistory(theConnection, theCursor, user_id):
        #runs a query that deletes every transaction record with the current user's userID
        myString = ("DELETE FROM history WHERE userID='" + user_id + "'")
        theCursor.execute(myString)
        theConnection.commit()
        #verification of deletion for testing purposes
        #print(theCursor.rowcount, "record(s) deleted.")
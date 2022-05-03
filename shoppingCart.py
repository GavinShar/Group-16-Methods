import mysql.connector
import sys

class shoppingCart:
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

    ## Creates the cart table
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE cart (ID int NOT NULL, Title varchar(25), Price int)")
        connection.commit()

    ## Prints the current items in the table
    def viewCart():
        query = "SELECT * FROM cart WHERE Title=%s"
        data = getTitle()
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()

    ## Emties the cart and records the contents in order history
    def checkoutCart():
        ## Needs to record contents of cart
        cursor = connection.cursor()
        cursor.execute("DROP TABLE cart")
        connection.commit()

    ## Adds queried item to cart
    def addToCart():
        query = "INSERT INTO cart (ID, Title, Price) Values (%s, %s, %s)"
        data = (getID(), getTitle(), getPrice())
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()

    ## Removes queried item from cart
    def removeFromCart():
        query = "DELETE FROM cart WHERE Title=%s"
        data = getTitle()
        cursor = connection.cursor(query, data)
        cursor.execute()
        connection.commit()

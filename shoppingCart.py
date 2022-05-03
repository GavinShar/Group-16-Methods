import mysql.connector
import sys

class shoppingCart:
    ## Connects to the database
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="")
        print("Successful connection.")

    except:
        print("Failed connection.")

    ## Creates the cart table
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE cart ()")
        connection.commit()

    ## Prints the current items in the table
    def viewCart():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cart")
        connection.commit()

    ## Emties the cart and records the contents in order history
    def checkoutCart():
        cursor = connection.cursor()
        cursor.execute("DROP TABLE cart")
        connection.commit()

    ## Adds queried item to cart
    def addToCart(item):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO cart (Columns) Values ()")
        connection.commit()

    ## Removes queried item from cart
    def removeFromCart(item):
        cursor = connection.cursor()
        cursor.execute("DELETE FROM cart")
        connection.commit()

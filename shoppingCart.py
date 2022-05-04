import mysql.connector
import sys
import random
from history import History

class shoppingCart:
    ## Prints the current items in the table
    def viewCart(connection, cursor, user_id):
        cursor.execute("SELECT ISBN FROM cart WHERE userID = '" + user_id + "'")
        result = cursor.fetchall()
        print("Items in your cart:")
        for x in result:
            print("ISBN:", x[0])

    ## Emties the cart and records the contents in order history
    def checkoutCart(connection, cursor, user_id):
        #Add items in user's cart to user's purchase history
        cursor.execute("SELECT ISBN FROM cart WHERE userID = '" + user_id + "'")
        result = cursor.fetchall()
        for x in result:
            History.addTransac(connection, cursor, user_id, x[0])
            cursor.execute("UPDATE item SET quantity = (quantity - 1) WHERE ISBN = '" + x[0] + "'")
            connection.commit()

        cursor.execute("DELETE FROM cart WHERE userID='" + user_id + "'")
        connection.commit()

    ## Adds queried item to cart
    def addToCart(connection, cursor, user_id, item):
        randID = random.randint(1, 1000)
        cursor.execute("INSERT INTO cart (id, userID, ISBN) VALUES (" + str(randID) + ", '" + user_id + "', '" + item + "')")
        connection.commit()

    ## Removes queried item from cart
    def removeFromCart(connection, cursor, user_id, item):
        cursor.execute("DELETE FROM cart WHERE userID='" + user_id + "' AND ISBN='" + item + "'")
        connection.commit()
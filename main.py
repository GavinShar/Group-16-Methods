from history import History
from shoppingCart import shoppingCart
import mysql.connector
import sys

## attempts to connect to the database
try:
    myConnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="methods_project"
    )

    print("Successful connection.")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

## cursor to send queries through
myCursor = myConnection.cursor()


is_not_logged = True
while True:
    user_in = 0
    while is_not_logged: #have this change to false after login
        try:
            user_in = int(input("1.Login\n2.Create Account\n3.Exit\n"))
            if 1 < user_in > 3:
                print("This is not a valid input please try again.")
                continue
            else:
                break
        except ValueError:
            print("This is not a valid input please try again.")
            continue

    if user_in == 1:
        print("Placeholder login")
        is_not_logged = False
    if user_in == 2:
        print("Placeholder Create Account")
        is_not_logged = False
    if user_in == 3:
        break
                            #after login
    while True:
        try:
            user_in = int(input("1.User Info\n2.Cart\n3.Inventory\n4.Exit\n"))
            if 1 > user_in or 4 < user_in:
                print("This is not a valid input please try again.")
                continue
        except ValueError:
            print("This is not a valid input please try again.")
            continue
        if user_in == 1:                    #user login loop
            print("Placeholder User Info")
            while True:
                try:
                    user_in = int(input("1.Go Back\n2.Login Details\n3.Shipping Information"
                                        "\n4.Payment Information\n5.Order History\n6.Edit User Information\n"))
                    if 1 > user_in or 6 < user_in:
                        print("This is not a valid input please try again.")
                        continue
                except ValueError:
                    print("This is not a valid input please try again.")
                    continue
                if user_in == 1:
                    break
                if user_in == 2:
                    print("Placeholder Edit Login")
                if user_in == 3:
                    print("Placeholder Edit Payment Info")
                if user_in == 4:
                    print("Placeholder Edit Shipping")
                if user_in == 5:
                    print("Placeholder Delete Account")
                if user_in == 6:
                    print("Placeholder Edit User Info")
                    while True:                         #edit user info loop
                        try:
                            user_in = int(input("1.Go Back\n2.Edit Login\n3.Edit Payment Info"
                                                "\n4.Edit Shipping Info\n5.Delete Account\n"))
                            if 1 > user_in or 5 < user_in:
                                print("This is not a valid input please try again.")
                                continue
                        except ValueError:
                            print("This is not a valid input please try again.")
                            continue
                        if user_in == 1:
                            break
                        if user_in == 2:
                            print("Placeholder Edit Login")
                        if user_in == 3:
                            print("Placeholder Edit Payment Info")
                        if user_in == 4:
                            print("Placeholder Edit Shipping")
                        if user_in == 5:
                            print("Placeholder Delete Account")
        if user_in == 2:                    #cart info loop
            print("Placeholder Cart Info")
            while True:
                try:
                    user_in = int(input("1.Go Back\n2.View Cart\n3.Remove Item from Cart"
                                  "\n4.Checkout\n"))
                    if 1 > user_in or 4 < user_in:
                        print("This is not a valid input please try again.")
                        continue
                except ValueError:
                    print("This is not a valid input please try again.")
                    continue
                if user_in == 1:
                    break
                if user_in == 2:
                    #print("Placeholder View Cart")
                    shoppingCart.viewCart(myConnection, myCursor, user_id)
                if user_in == 3:
                    #print("Placeholder Remove Item from Cart")
                    user_in = str(input("Enter the ISBN for the book you would like to remove from your cart: "))
                    shoppingCart.removeFromCart(myConnection, myCursor, user_id, user_in)
                if user_in == 4:
                    #print("Placeholder Checkout")
                    shoppingCart.checkoutCart(myConnection, myCursor, user_id)
                    break

        if user_in == 3:                        #inventory loop
            #print("Placeholder Inventory")
            myCursor.execute("SELECT * FROM item")
            result = myCursor.fetchall()
            for x in result:
                print()
                print("ISBN: ", x[0])
                print("Title: ", x[1])
                print("Author: ", x[2])
                print("Quantity: ", x[4])
                print("Price: ", x[5])
            while True:
                try:
                    user_in = int(input("1.Go Back\n2.Add book to cart\n"))
                    if 1 > user_in or 2 < user_in:
                        print("This is not a valid input please try again.")
                        continue
                except ValueError:
                    print("This is not a valid input please try again.")
                    continue
                if user_in == 1:
                    break
                if user_in == 2:
                    user_in = str(input("Enter the ISBN for the book you would like to add to your cart: "))
                    shoppingCart.addToCart(myConnection, myCursor, user_id, user_in)
                    break
        if user_in == 4: #exit
            break
    if user_in == 4: break

## close the cursor and connection once you're done
myCursor.close()
myConnection.close()
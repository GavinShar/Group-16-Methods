from history import History
from shoppingCart import shoppingCart
from user_info import user_info
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
deleted = False
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
        while is_not_logged:
            user_id = str(input("User ID: "))
            user_in = str(input("Password: "))
            is_not_logged = user_info.user_login(myConnection, myCursor, user_id, user_in)
    if user_in == 2:
        user_id = str(input("Enter user ID: "))
        passwd = str(input("Enter password: "))
        cardNum = str(input("Enter credit card number: "))
        cardExp = str(input("Enter card expiration date (MM/YY): "))
        cardCVV = str(input("Enter card CVV: "))
        address = str(input("Enter street address: "))
        city = str(input("Enter city: "))
        state = str(input("Enter state: "))
        usrZip = str(input("Enter zip: "))
        user_info.create_user(myConnection, myCursor, user_id, passwd, cardNum, cardExp, cardCVV, address, city, state, usrZip)
        is_not_logged = False
    if user_in == 3:
        break
                            #after login
    while True:
        if deleted:
            break
        try:
            user_in = int(input("1.Edit user\n2.Cart\n3.Inventory\n4.Exit\n"))
            if 1 > user_in or 4 < user_in:
                print("This is not a valid input please try again.")
                continue
        except ValueError:
            print("This is not a valid input please try again.")
            continue
        if user_in == 1:      #edit user loop
            while True:
                try:
                    user_in = int(input("1.Go Back\n2.Login Details\n3.Shipping Information"
                                        "\n4.Payment Information\n5.Order History\n6.Delete account\n"))
                    if 1 > user_in or 6 < user_in:
                        print("This is not a valid input please try again.")
                        continue
                except ValueError:
                    print("This is not a valid input please try again.")
                    continue
                if user_in == 1:
                    break
                if user_in == 2:
                    user_in = str(input("Enter new password: "))
                    user_info.edit_login(myConnection, myCursor, user_id, user_in)
                if user_in == 3:
                    address = str(input("Enter new street address: "))
                    city = str(input("Enter new city: "))
                    state = str(input("Enter new state: "))
                    usrZip = str(input("Enter new zip: "))
                    user_info.edit_shipping(myConnection, myCursor, user_id, address, city, state, usrZip)
                if user_in == 4:
                    cardNum = str(input("Enter new credit card number: "))
                    cardExp = str(input("Enter new card expiration date (MM/YY): "))
                    cardCVV = str(input("Enter new card CVV: "))
                    user_info.edit_payment(myConnection, myCursor, user_id, cardNum, cardExp, cardCVV)
                if user_in == 5:
                    History.viewHistory(myConnection, myCursor, user_id)
                if user_in == 6:
                    user_in = str(input("Are you sure you want to delete your account? (y/n): "))
                    if user_in == 'y':
                        user_info.delete_account(myConnection, myCursor, user_id)
                        print("Account deleted; exiting program")
                        myCursor.close()
                        myConnection.close()
                        sys.exit()
                    else:
                        print("Account deletion aborted")
                    
        if user_in == 2:                    #cart info loop
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
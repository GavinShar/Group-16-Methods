#put classes here

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
                                  "\n4.Checkout\n5.Add Item to Cart\n"))
                    if 1 > user_in or 5 < user_in:
                        print("This is not a valid input please try again.")
                        continue
                except ValueError:
                    print("This is not a valid input please try again.")
                    continue
                if user_in == 1:
                    break
                if user_in == 2:
                    print("Placeholder View Cart")
                if user_in == 3:
                    print("Placeholder Remove Item from Cart")
                if user_in == 4:
                    print("Placeholder Checkout")
                if user_in == 5:
                    print("Placeholder Add Item to Cart")

        if user_in == 3:                        #inventory loop
            print("Placeholder Inventory")
            while True:
                try:
                    user_in = int(input("1.Go Back\n2.Cat1\n3.Cat2"
                                  "\n4.Cat3\n5.Cat4\n"))
                    if 1 > user_in or 5 < user_in:
                        print("This is not a valid input please try again.")
                        continue
                except ValueError:
                    print("This is not a valid input please try again.")
                    continue
                if user_in == 1:
                    break
                if user_in == 2:
                    print("Placeholder Cat1")
                if user_in == 3:
                    print("Placeholder Cat2")
                if user_in == 4:
                    print("Placeholder Cat3")
                if user_in == 5:
                    print("Placeholder Cat4")
        if user_in == 4: #exit
            break
    if user_in == 4: break
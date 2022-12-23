itemstock = [{"idnum":0, "name":'Water', "price":9}, #The list to store the items in stock
            {"idnum":1, "name":'Soda' ,"price":14},
            {"idnum":2, "name": 'Juice', "price":13},
            {"idnum":3, "name": 'Energy Drink', "price":17},
            {"idnum":4, "name": 'Milk', "price":15}]

selecteditems = [] # An empty list to store the selected items in
totalcost = 0 # To be used for the computing of the total amount cost

print("\n-------------    WELCOME TO THE PYTHON BEVERAGE VENDING MACHINE!    ---------------") #The code to introduce the program to the user
print("")
print("------------ Here you'll be able to pick your desired item --------------")
print("------------  from the Menu, enter your credits, confirm   --------------")
print("------------ your purchase, and enjoy your item of choice! --------------\n")
print("------------          Here is the menu down below:          --------------\n")


for a in itemstock:
    print(F"| ID: {a['idnum']} |   | ITEM: {a['name']} |   | PRICE: {a['price']} |\n") #To display the menu

creds = int(input("Please insert desired amount of credits: ")) # Recieves the amount of credits from the user
print("\n-------------   You have entered", creds, "credits.      --------------\n") # Outputs the amount inputted


choice = int(input("Now, choose an item ID from the Menu and enter the ID: ")) #To display the option to choose the desired item
for a in itemstock:
    if choice > 4: #To prevent the user from entering invalid code and the program continuing anyway.
        print("\nInvalid code.")
        quit()
    if choice == a['idnum']: #TO check if the choice is a valid option and is part of the menu
        selecteditems = a
        print(F"\n------------   You have selected {a['name']}   --------------")
        if creds < a['price']: #To check if the user entered enough funds
            print("\nUnfortunately, you have insufficient funds.")
            quit()
        elif creds >= a['price']: #To show the user that the item has been bought and they can buy the item
            totalcost = a['price'] + totalcost
            print("\nYou have the sufficient credits to buy the item.")
            print(F"\nThe cost will be {a['price']} credits.")


print("\n------------    Would you like to print your reciept?     ------------\n") #To ask the user if they would like the reciept
reciept = input("y for Yes, n for No: ")
if reciept == "y": #For if the option is yes, and to print the reciept
    print("\nYour credits entered was:", creds)
    print(F"\nYour chosen item was:", selecteditems['name'])
    print("\nAnd your total change is:", creds - totalcost)
    print(F"\n------------   You have just recieved:",selecteditems['name'],"!   ------------")
elif reciept == "n": #If they would not like to print the reciept, it will show the item chosen only
        print(F"\n------------   You have just recieved:",selecteditems['name'],"!   ------------")
        quit()
else:
    print("\nUnrecognized option.") #If the option is neither yes or no, but will still display the item though without the reciept
    print(F"\n------------   You have just recieved:", selecteditems['name'], "!   ------------")
    quit()

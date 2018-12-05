#print Welcome to the restaurant menu program
print("Welcome to the Restauratron_3000")

#create empty dictionary
menu_dict = {}

#Start loop for input
while True:
    #Ask user to enter the dish
    dish = input("Please enter a dish for the menu: ")
    #Ask user to enter the price
    price = input("Please enter a price for the dish: ")
    #print added menu item
    print ("Your dish is " + dish + " and costs " + price + " Euro")

    #add price to menu item
    menu_dict[dish] = price

    #Ask user to add another item to dictionary
    new = input("Would you like to input a new dish? (y/n): ")

    #break or continue loop
    new = new.lower()
    if new == "n" or new == "no":
        break

#print menu

print("Today's menu is: ")
for food in menu_dict:
    print(" - " + food + " - " + menu_dict[food] + " Euro")


#write menu to file

with open("Menu.txt", "w+") as menu_file:
    menu_file.write("Today's menu is: ")
    for food in menu_dict:
        menu_file.write("\n - " + food + " - " + menu_dict[food] + " Euro")
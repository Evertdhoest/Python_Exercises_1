while True:
    string = input("Enter your message: ")
    print (string.lower())
    cont = input("Would you like to continue y/n: ").lower()
    if cont == "yes" or cont == "y":
        continue
    else:
        print("Thank you for using LowercaseConvert_3000!")
        break
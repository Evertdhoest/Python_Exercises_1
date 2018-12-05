first = True
number = 0
while number < 1 or number > 100 or type(number) == str:
    number = input("Choose a number between 1 and 100: ")
    if number.isdigit():
        number = int(number)
        for i in range(1, int(number)):
            if i % 3 == 0 and i % 5 == 0:
                print("Fizzbuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    else:
        print("Please enter an integer between 1 and 100")
        break


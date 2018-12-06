number = input("Select a number between 1 and 100: ")

start = 1

while not number.isdigit() or (int(number) < 1 or int(number) > 100):
    print("This input is incorrect")
    number = input("Select a number between 1 and 100: ")

number = int(number)
while start <= number:
    if (start % 3) and (start % 5) == 0:
        print("Fizzbuzz")
    elif (start % 3) == 0:
        print("Fizz")
    elif (start % 5) == 0:
        print("Buzz")
    else:
        print(str(start))
    start += 1
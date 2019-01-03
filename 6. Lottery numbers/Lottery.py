## import random

from random import randint

##Create empty lottery numbers list

def generate_numbers_list(amount):
    numbers_list = []

##Create random numbers and append list

    while True:
        if len(numbers_list) == amount:
            break

        lot_number = randint(1, 100)

        if lot_number not in numbers_list:
            numbers_list.append(lot_number)

    return numbers_list

## Welcome

print("Welcome to the lottery numbers generator")

## Ask amount of lottery numbers

input_numbers = input("Please enter how many random numbers you would like to have (max 10): ")

## Check if amount is valid

while not input_numbers.isdigit() or int(input_numbers) < 1 or int(input_numbers) > 10:
    print("This input is incorrect")
    input_numbers = input("Please choose a number between 1 and 10: ")
    continue

## return random numbers 'amount' times

input_numbers = int(input_numbers)

print (generate_numbers_list(input_numbers))


#!/usr/bin/python3
def fizzbuzz():
    for idx in range(1, 101):
        if (idx % 3 == 0 and idx % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (idx % 3 == 0 and idx % 5 != 0):
            print("Fizz", end=' ')
        elif (idx % 3 != 0 and idx % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(f"{idx:d}", end=' ')

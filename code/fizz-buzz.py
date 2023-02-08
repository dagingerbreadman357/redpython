#!/usr/bin/env python3

number =  int(input("How many values should we process: "))


for x in range(1, number + 1):
    pass
    if x % 3 ==0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 ==0:
        print("Fizz")
    elif x % 5 ==0:
        print("Buzz")
    else:
        print(x)
    
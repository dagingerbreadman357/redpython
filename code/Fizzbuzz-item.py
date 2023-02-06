#!/usr/bin/env python3

# Python implementation here

value = int(input("Enter an integer value: "))

# Print FizzBizz if the value is a multiple of Three or Five

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")

# Print Buzz if value is multiple of Five
elif value % 5 == 0:
    print("Buzz")

# Print Fizz if value is multiple of Three
elif value % 3 == 0:
    print("Fizz")

# If value doesnt match any condition print value
else:
    print(value)

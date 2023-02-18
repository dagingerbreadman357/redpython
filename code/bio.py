#!/bin/env python3.7

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")              #this is just a test
# print("and loves the color " + color + ".", end=" ")

# end= " " puts space at the end of each line
# sep= " " using this can put space between each operand
# sep= ", " using this can put commas between each operand

print(name, "is", age, "years old and loves the color", color + ".")

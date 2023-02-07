#!/usr/bin/env python3

# while CONDITIONS:
#    print("Something")

# This will be an infinite loop because 1 will always be less than 2
# the condition in the loop needs to be dynamic if we want to stop the loop

#  while 1 < 2:
#      print('something')

# We have a loop with a condition with an iteration that modifies the count variable
#  once the variable is modified to = 5 the loop should stop

count = 1

while count <= 4:
    print("looping")
    count += 1
    
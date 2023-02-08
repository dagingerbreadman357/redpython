#!/usr/bin/env python3


# 'while' loop with if statement nested

counter=1                 # variable

while counter <= 25:      # as long as counter is 25 or less
    if counter % 4 ==0:   # if the counter is divisable by 4 *evenly*
       print(counter)     # show the value of the variable counter
    counter += 1          # iterate through by adding 1 to the value of counter and saving as new counter value
    
    
# remeber to indent properly based on the context we have

# 'for' loop with if statement nested

print('\n')                   # creating space

colors = ['red', 'blue', 'green', 'brown']

for color in colors: 
    if color == 'blue':
        continue
    elif color == 'brown':
        break
    print(color)
    
print('\n')                   # creating space

# intergrating 'else' with loops

cars = ['lincoln', 'bmw', 'honda', 'chevy']

for model in cars:                    
    if model == 'ford':                       # will keep looping through list until either it finds ford or gets to end of list
        print('Im a Ford man')                # prints this if ford is found
        break                                 # then breaks out of loop
else:
    print('I dont like any of these companies')   # if ford is not found after going through entire list it will hit the else and print it.


# *else* is mainly used only when using *break* in a loops



# Using range function


print('\n')                   # creating space

my_range = range(0, 25, 2)   # creating a range of number 0-24 iterating by 2

print('\n')                   # creating space

print(list(my_range))        # turning my_range into a list 0-24 iterating by 2

print('\n')


# List Comprehensions

colors = ['red', 'black', 'blue', 'green', 'yellow']

uppercase_colors = []

print

for color in colors:
    uppercase_colors.append(color.upper())
    
print(uppercase_colors)
    
    
print('\n')


# simpler way to do the same as above

vdoms = ['aoc', 'doc', 'dshs', 'hca', 'dor']

uppercase_vdoms = [fw.upper() for fw in vdoms]

print(uppercase_vdoms)



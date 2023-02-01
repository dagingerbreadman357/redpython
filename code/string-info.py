#!/usr/bin/env python3.7

message = input("Enter a message: ")

print("First character:", message[0])
print("Second character:", message[-1])
print("Middle character:", message[int(len(message) / 2)])
print("Even Characters:", message[0::2])
print("Odd Characters:", message[1::2])
print("Message in reverse:", message[::-1])
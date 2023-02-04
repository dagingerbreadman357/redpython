#!/usr/bin/env python3.7


# I will be creating a list of AWS services and populating it into an empty list

# Start with an empty list

services = []
print(services)


# Populate the services list with services from AWS using append

services.append("S3")
services.append("X-Ray")
services.append("ECS")
services.append("Beanstalk")
services.append("IAM")
services.append("LAMBDA")

# Print the list and length of the list

print(services)
print("There are", len(services), "services on this list")

# Remove two specific services from the list by index

del services[2:4]

# Print new list and length of list

print(services)
print("There are now ", len(services), "services in the list.")
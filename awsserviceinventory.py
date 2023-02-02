#!/usr/bin/env python3.7


# I will be creating a list of AWS services and populating it into an empty list

# The list will start out empty

services = []
print(services)
# I will now populate the services list with services from AWS

services.append("S3")
services.append("X-Ray")
services.append("ECS")
services.append("Beanstalk")
services.append("IAM")
services.append("LAMBDA")

# Now I will print out the list and length of the list

print(services)
print("There are", len(services), "services on this list")

# Remove two specific services from the list

del services[2:4]

# Print new list and length of list

print("The new list of services", services, "with a quantity of", len(services), "services.")
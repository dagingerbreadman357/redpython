#!/usr/bin/env python3

# week 13 project

import os

path = "/home/ec2-user/environment/redpython"

files_list = os.listdir(path)

for dir in files_list:
    if dir == '.git':
        print(path, dir.append())
    

#file_size = {'.git': 220, '.gitignore': 1.8, 'hello_keon.py': 31, 'hello_world.py': 33, 'list-script.py': 177, 'random_name_generator.py': 0, 'README.md': 101, 'awsserviceinventory.py': 691, 'code': 334}
#print(file_size)
    



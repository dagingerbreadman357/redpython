#!/usr/bin/env python3

# week 13 project
import os


path = os.chdir("/home/ec2-user/environment/redpython/code/")


dir_list = list(os.listdir(path))

for path in os.listdir():
    dict_list = {}                   
    dict_list['path'] = os.path.realpath(path)
    file_size = os.stat(path) 
    dict_list['size'] = file_size.st_size
    print(dict_list)

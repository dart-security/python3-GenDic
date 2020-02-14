#!/usr/bin/python
# Dart-Security
# BY: Equinockx

import itertools
import os

print("Enter the name of File(dictionary): ", end=" ")
_name = input()
print("Enter the characters : ", end=" ")
_character = input()
print("Enter the number of characters for each line: ", end=" ")
_rep = input() # here enter like a string
_number = int(_rep) # here parsing the string to int

_file_name = _name + ".txt"

dic = itertools.product(_character, repeat=_number)


for i in dic:
    f = open(_file_name,"a")
    f.write(str(''.join(i)) + os.linesep)
    f.close()
    # print ''.join(i)

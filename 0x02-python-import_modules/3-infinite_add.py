#!/usr/bin/python3

from sys import argv

sum = 0
for i in range(len(argv) - 1):
    sum += int(argv[i + 1])

print("{}".format(sum))

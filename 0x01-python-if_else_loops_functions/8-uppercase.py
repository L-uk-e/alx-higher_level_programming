#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            s = chr(ord(str[x]) - 32)
        else:
            s = str[x]
        print("{}".format(s), end="")
    print("\n", end = "")

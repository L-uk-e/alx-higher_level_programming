#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    while count < x:
        try:
            print(my_list[count], end="")
            count += 1

        except IndexError:
            #print("The list doesn't contain any more values", end="")
            break

        except:
            #print("An unknown error has occured", end="")
            break
    print()

    return count

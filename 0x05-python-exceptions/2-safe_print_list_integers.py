#!/usr/bin/python3

def safe_print_list_integers(mylist=[], x=0):
    count = 0
    idx = 0

    while count < x:
        try:
            print("{:d}".format(mylist[idx]), end="")
            count += 1
            idx += 1

        except (ValueError, TypeError):
            idx += 1
            continue

        except IndexError:
            break
    print()

    return count

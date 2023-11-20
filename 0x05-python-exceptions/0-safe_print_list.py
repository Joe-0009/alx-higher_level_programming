#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    numb_of_x = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i], end=""))
            numb_of_x += 1
    except IndexError:
        break

    print()

    return numb_of_x
        


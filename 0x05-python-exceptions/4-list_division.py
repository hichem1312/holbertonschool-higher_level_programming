#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    i = 0
    x = 0
    while i < list_length:
        try:
            x = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            x = 0
        except TypeError:
            print("wrong type")
            x = 0
        except IndexError:
            print("out of range")
            x = 0
        finally:
            newlist.append(x)
            i += 1
    return(newlist)

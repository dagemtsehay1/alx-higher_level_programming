#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in my_list:
        while my_list.count(i) > 1:
            my_list.pop(my_list.index(i))
    sum = 0
    for i in my_list:
        sum += i
    return sum

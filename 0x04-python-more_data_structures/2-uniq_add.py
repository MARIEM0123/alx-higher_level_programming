#!/usr/bin/python3
def uniq_add(my_list=[]):

    nq_lst = set(my_list)
    n = 0

    for i in nq_lst:
        n += i

    return (n)

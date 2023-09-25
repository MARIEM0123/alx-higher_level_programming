#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """the function to divide two lists

    Args:
        my_list_1: The first parameter
        my_list_2: The second parameter
        list_length: The number

    Returns:
        there is a return
    """
    n_lst = []
    for i in range(0, list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            x = 0
        except ZeroDivisionError:
            print("division by 0")
            x = 0
        except IndexError:
            print("out of range")
            x = 0
        finally:
            n_lst.append(x)
    return (n_lst)

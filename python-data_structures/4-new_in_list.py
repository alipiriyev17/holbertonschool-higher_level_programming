#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copy of a list at a specific position."""
    new_list = my_list.copy()

    if idx < 0:
        return new_list
    if idx >= len(new_list):
        return new_list

    new_list[idx] = element
    return new_list

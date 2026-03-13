#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character."""
    length = len(sentence)

    if length == 0:
        return (0, None)

    return (length, sentence[0])

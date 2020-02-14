def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    # hello
    # 2 llo he
    # -2 lo hel
    
    l = len(string)

    n = n%l

    if n > 0:
        d = l-n-1
    else:
        d = n

    rotated_string = string[d:] + string[0:d]
    
    return rotated_string
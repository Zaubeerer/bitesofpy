def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    
    with open(filepath, "rb") as f:
        list_of_lines = f.readlines()

    list_of_lines = [s.decode("utf-8").rstrip('\n') for s in list_of_lines]

    return list_of_lines[-n:]
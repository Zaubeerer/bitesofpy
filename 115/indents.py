def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    
    for n_leading_spaces, s in enumerate(text):
        if s != " ":
            return n_leading_spaces


ALPHANUMERIC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def is_alphanumeric(character):
    if str(character) == "":
        return False
    else:
        return str(character) in ALPHANUMERIC


def get_index_different_char(chars):

    list_of_type = [is_alphanumeric(char) for char in chars]

    if sum(list_of_type) > 1:
        return list_of_type.index(False)
    else:
        return list_of_type.index(True)

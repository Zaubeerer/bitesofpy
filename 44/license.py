import secrets
import string

ALPHABET = string.ascii_letters + string.digits

def gen_key(parts=4, chars_per_part=8):
    key_parts = ["".join([secrets.choice(ALPHABET).upper() for i in range(chars_per_part)])
                    for _ in range(parts)]
    return  "-".join(key_parts)

import re
import string

string


def strip_comments(code):
    # 1. Strip multi-line comments / docstrings
    stripped_code = re.sub(r"[ ]*([\"]{3}[\n]?)[\s\S]*?([\"]{3}[\n]?)", "", code)

    # 2. Strip one-line / in-line comments
    stripped_code = re.sub(r"(?!.*[\'\"].*\n)[ ]*#.*?\n", "", stripped_code)

    return stripped_code

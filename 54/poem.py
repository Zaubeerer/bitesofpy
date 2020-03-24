INDENTS = 4

import io


def print_hanging_indents(poem):
    stripped_lines = [line.strip() for line in poem.split("\n")]

    nice_poem = ""
    indent = ""

    for line in stripped_lines:
        if line == "":
            indent = ""  # eliminate indent, don't print empty line
        else:
            nice_poem += f"{indent}{line}\n"

            indent = "    "  # indent

    print(nice_poem)

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    n_names = 0
    for name in names:
        if not name.startswith(IGNORE_CHAR):
            if not any(char.isdigit() for char in name):
                if name.startswith(QUIT_CHAR):
                    break
                if n_names == 5:
                    break
                n_names += 1
                yield name

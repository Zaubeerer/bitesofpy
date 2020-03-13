import sys
from itertools import cycle
from time import sleep, time

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    
    spinner = cycle(SPINNER_STATES)

    time_limit = time() + seconds

    while time() < time_limit:
        # TODO: why does flush=True not work?
        # print(f"\r{next(spinner)}", flush=True)
        sys.stdout.write(f"\r{next(spinner)}") # no newline
        sys.stdout.flush()
        sleep(STATE_TRANSITION_TIME)

if __name__ == '__main__':
    spinner(2)

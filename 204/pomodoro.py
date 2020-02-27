import time

# ONE_MIN = 60
# FIVE_MIN = ONE_MIN * 5
# TWENTY_FIVE_MIN = ONE_MIN * 25
# THIRTY_MIN = ONE_MIN * 30
# HOUR = ONE_MIN * 60
# CURRENT_SESSION = 1

ONE_MIN = .006
FIVE_MIN = ONE_MIN * .0005
TWENTY_FIVE_MIN = ONE_MIN * .0025
THIRTY_MIN = ONE_MIN * .003
HOUR = ONE_MIN * .06
CURRENT_SESSION = 1


def break_time(delay, loop):
    """Break time

    :param delay: float of delay in seconds
    :param loop: int of the current loop
    :return: None
    """
    _delay = int(delay / ONE_MIN)
    print(f"[{loop}] {time.strftime('%X')} Time for a {_delay} min break!")
    time.sleep(delay)


def lunch_time(delay):
    """Lunch time

    :param delay: float of delay in seconds
    :return: None
    """
    print(f"\n** {time.strftime('%X')} Time for lunch! **")
    time.sleep(delay)


def work_time(delay, loop):
    """Work time

    :param delay: float of delay in seconds
    :param loop: int of the current loop
    :return: None
    """
    print(f"[{loop}] {time.strftime('%X')} Time to work!")
    time.sleep(delay)


def session(
    work_length=TWENTY_FIVE_MIN,
    short_break_length=FIVE_MIN,
    long_break_length=THIRTY_MIN,
):
    """Session

    :param work_length: float of work length in seconds
    :param short_break_length: float of short break length in seconds
    :param long_break_length: float of long break length in seconds
    :return: None
    """
    loop = 1

    while loop < 4:
        work_time(work_length, loop)
        break_time(short_break_length, loop)
        loop += 1

    work_time(work_length, loop)

    if CURRENT_SESSION % 2 != 0:
        break_time(long_break_length, loop)


def main(
    work_length=TWENTY_FIVE_MIN,
    short_break_length=FIVE_MIN,
    long_break_length=THIRTY_MIN,
    lunch_length=HOUR,
):
    """Main entry point

    :param work_length: float of work length in seconds
    :param short_break_length: float of short break length in seconds
    :param long_break_length: float of long break length in seconds
    :param lunch_length: float of lunch length in seconds
    :return: None
    """
    global CURRENT_SESSION
    print(f"Pomodor timer started at: {time.strftime('%X')}")

    while CURRENT_SESSION <= 4:
        print(f"\nSession: {CURRENT_SESSION}")
        session(work_length, short_break_length, long_break_length)
        if CURRENT_SESSION == 2:
            lunch_time(lunch_length)
        CURRENT_SESSION += 1

    print(f"\n{time.strftime('%X')} Time to go home!")

    print(f"\nWork day completed at: {time.strftime('%X')}")


if __name__ == "__main__":
    main()
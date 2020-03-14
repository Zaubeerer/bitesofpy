from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    finish_100days = start_100days + timedelta(days=100)

    return finish_100days.strftime("%Y-%m-%d")


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    timedelta = pycon_date - pybites_founded

    return timedelta.days

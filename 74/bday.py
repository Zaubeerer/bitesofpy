import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[calendar.weekday(date.year, date.month, date.day)]

import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        # you complete

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)
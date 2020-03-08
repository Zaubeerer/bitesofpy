import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    totals = itertools.accumulate(sequence)

    return [round(total / (i + 1), 2) for i, total in enumerate(totals)]

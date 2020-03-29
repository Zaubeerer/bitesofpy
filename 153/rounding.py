def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        return [int(value) + 1 for value in transactions]
    else:
        return [int(value) for value in transactions]

def get_profile(*args, name="julian", profession="programmer"):
    if len(args) > 0:
        raise TypeError

    return f'{name} is a {profession}'

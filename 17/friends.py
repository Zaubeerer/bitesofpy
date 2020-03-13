from itertools import combinations, combinations_with_replacement, permutations


def friends_teams(friends, team_size=2, order_does_matter=False):

    if order_does_matter:
        return permutations(friends, r=team_size)
    else:
        return combinations(friends, r=team_size)

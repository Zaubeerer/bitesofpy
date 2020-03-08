from itertools import combinations, permutations


def find_number_pairs(numbers, N=10):
    return list(gen_combinations_with_sum_N(numbers, N=N))


def gen_combinations_with_sum_N(numbers, N=10):
    for comb in combinations(numbers, r=2):
        if sum(comb) == N:
            yield comb

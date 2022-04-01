from itertools import product


def solution(numbers, target):
    number_set = list((number, -number) for number in numbers)
    # [(4, -4), (1, -1), (2, -2), (1, -1)]
    number_product = product(*number_set)
    # *을 사용하면 unpacking을 한다.
    # https://peps.python.org/pep-0448/#rationale
    # [(4, 1, 2, 1), (4, 1, 2, -1), (4, 1, -2, 1), (4, 1, -2, -1), (4, -1, 2, 1) ...]
    number_sums = list(map(sum, number_product))
    # [8, 6, 4, 2, 6, 4, 2, 0, 0, -2, -4, -6, -2, -4, -6, -8]
    return number_sums.count(target)


# print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))
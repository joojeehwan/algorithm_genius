"""
most_common() 이라는 함수가 있다니... 첨 알았다
매개변수를 넣으면 그 순위까지만 반환한다. 없으면 전부 반환한다.
예를 들어 most_common(3)이면 가장 많이 나온 순서대로 3개까지만 반환한다.
Counter('abracadabra').most_common(3)
=> [('a', 5), ('b', 2), ('r', 2)]
"""

import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        # most ordered 생긴거
        # [(('A', 'D'), 3), (('C', 'D'), 3), (('A', 'B'), 2),
        # (('A', 'C'), 2), (('A', 'E'), 2), (('D', 'E'), 2),
        # (('X', 'Y'), 2), (('X', 'Z'), 2), (('Y', 'Z'), 2),
        # (('B', 'C'), 1), (('B', 'D'), 1), (('B', 'E'), 1),
        # (('C', 'E'), 1)]
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

order_string = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course_string = [2,3,5]
print(solution(order_string, course_string))
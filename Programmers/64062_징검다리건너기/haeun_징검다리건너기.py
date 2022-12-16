"""
ㅜㅜ 쉬운거네 어이없다..
근데 세그먼트 트리 풀이는 뭐지..
"""

def solution(stones, k):
    start, end = 1, max(stones)
    mid = (start + end) // 2

    while start < end:
        zeros = 0

        for stone in stones:
            if stone - mid <= 0:
                zeros += 1
                if zeros >= k:
                    break
            else:
                zeros = 0

        if zeros >= k:
            end = mid
        else:
            start = mid + 1
        mid = (start + end) // 2

    return mid


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([10, 21, 76, 345, 19, 44, 1], 3))
print(solution([200000000, 19999], 1))
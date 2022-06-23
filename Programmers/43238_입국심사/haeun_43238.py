"""
어려워서 짜증나 죽겠네
https://programmers.co.kr/questions/21374
"""


def solution(n, times):
    low = 0
    high = n * max(times)
    while low < high:
        mid = (high + low) // 2
        people = 0
        for time in times:
            people += mid // time
        # print(f"people : {people} | mid : {mid} | low : {low} | high : {high}")
        if people >= n:
            high = mid
        else:
            low = mid + 1
    return high  # low여도 상관 없음

print(solution(6, [7, 10]))
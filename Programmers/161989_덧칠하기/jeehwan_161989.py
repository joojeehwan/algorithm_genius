def solution(n, m, section):
    #     answer = 0
    #     lst = [False] * n
    #     for target in section:
    #         lst[target - 1] = True

    #     i = 0
    #     while i < n :

    #         if lst[i]:

    #             for j in range(m):
    #                 if i + m < n:
    #                     lst[i+j] = True
    #                 i += m
    #             answer += 1

    answer = painted = 0

    for target in section:
        # 칠해지지 않은 곳의 taget만을 대상
        if target >= painted:
            # target 부터 m만큼 칠했음을 표시 
            painted = target + m
            answer += 1
    return answer
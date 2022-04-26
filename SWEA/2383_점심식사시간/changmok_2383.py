# 콩시간 십콩분

import itertools


for t in range(1, int(input())+1):
    n = int(input())
    floor = [list(map(int, input().split())) for _ in range(n)]
    humans = []
    stairs = []
    answer = 9876543210
    for r in range(n):
        for c in range(n):
            if floor[r][c] == 1:
                humans.append((r, c))
            elif floor[r][c] >= 2:
                stairs.append((r, c, floor[r][c]))

    s1r, s1c, s1w = stairs[0]
    s2r, s2c, s2w = stairs[1]

    lh = len(humans)
    for num in range(lh+1):
        s1_going_cases = itertools.combinations(humans, num)
        for s1_going_case in s1_going_cases:
            mid_result = 0
            s1 = []
            s2 = []
            for hr, hc in humans:
                if (hr, hc) in s1_going_case:
                    rt = abs(hr - s1r) + abs(hc - s1c)
                    s1.append((rt, hr, hc))
                else:
                    rt = abs(hr - s2r) + abs(hc - s2c)
                    s2.append((rt, hr, hc))
            s1.sort()
            s2.sort()

            stairQ = [0] * 200
            for reach_time, hr, hc in s1:
                while stairQ[reach_time + 1] >= 3:
                    reach_time += 1
                for time in range(reach_time + 1, reach_time + 1 + s1w):
                    stairQ[time] += 1
                mid_result = max(mid_result, reach_time + 1 + s1w)

            stairQ = [0] * 200
            for reach_time, hr, hc in s2:
                while stairQ[reach_time + 1] >= 3:
                    reach_time += 1
                for time in range(reach_time + 1, reach_time + 1 + s2w):
                    stairQ[time] += 1
                mid_result = max(mid_result, reach_time + 1 + s2w)
            answer = min(answer, mid_result)

    print(f'#{t} {answer}')
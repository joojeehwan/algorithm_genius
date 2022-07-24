'''

마법사 상어와 파이어볼

'''

N, M, K = map(int, input().split())
fireballs = []

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireballs.append([r-1, c-1, m, s, d])


MAP = [[[] for _ in range(N)] for _ in range(N)]

#상 부터 오른쪽으로 순서대로 8방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

#상어가 파이어볼 이동을 K번만큼
for _ in range(K):

    #파이어볼 이동
    while fireballs:
        curent_row, curent_col, curent_mass, curent_dir, curent_speed = fireballs.popleft()
        # 1번 - N번 행이 연결되어 있기 떄문에
        next_row = (curent_row + curent_speed * dr[curent_dir] % N)
        next_col = (curent_col + curent_speed * dc[curent_dir] % N)
        MAP[next_row][next_col].append([curent_mass, curent_speed, curent_dir])


        #2개 이상인지 체크
        for r in range(N):
            for c in range(N):
                #2개 이상인 경우 => 4개의 파이어볼로 쪼개기
                if len(MAP[r][c]) > 1:
                    sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])

                    while MAP[r][c]:
                        # 그 낱개 하나의 파이어볼 보는 거자나! pop으로 뺴서!
                        _m, _s, _d = MAP[r][c].pop(0)
                        sum_m += _m
                        sum_s += _s
                        if _d % 2:
                            cnt_odd += 1
                        else:
                            cnt_even += 1
                    if cnt_odd == cnt or cnt_even == cnt : #모두 홀수 이거나 모두 짝수인 경우
                        nd = [0, 2, 4, 6]

                    else:
                        nd = [1, 3, 5, 7]

                    if sum_m//5:
                        for d in nd:
                            fireballs.append([r, c, sum_m // 5, sum_s // cnt, d])

                # 1개인 경우
                if len(MAP[r][c]) == 1:
                    fireballs.append([r, c] + MAP[r][c].pop())

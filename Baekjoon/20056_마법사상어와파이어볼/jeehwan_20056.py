'''

마법사 상어와 파이어볼



N * N 격자에서 파이어볼 M개를 발사

파이어볼은 각자의 위치에서 이동을 대기

=> i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

격자의 행과 열은 1번 부터 N번까지의 번호가 매겨져 있고, 1번행은


1. 파이어볼의 이동

모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.

7	0	1
6	 	2
5	4	3

2. 파이어볼 이동후 행동

- 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
- 파이어볼은 4개의 파이어볼로 나누어진다.
- 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
    a. 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
    b. 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
    c. 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
- 질량이 0인 파이어볼은 소멸되어 없어진다.

'''

N, M, K = map(int, input().split())
fireballs = []

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireballs.append([r-1, c-1, m, s, d])


# 해당 문제도 지금, 이차원 배열 속에 하나의 값이 배열인 형태로 MAP을 구성
# MAP[next_row][next_col].append([curent_mass, curent_speed, curent_dir])
MAP = [[[] for _ in range(N)] for _ in range(N)]
#상 부터 오른쪽으로 순서대로 8방향 => why?!문제에서 0번이 지금 상이고 7번이 좌상으로 주어짐
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

#상어가 파이어볼 이동을 K번만큼
for _ in range(K):

    #1. 파이어볼의 이동 => 파이어볼을 초기에 다 넣어놓고, 하니씩 뺴면서 시물레이션을 진행

    while fireballs:
        curent_row, curent_col, curent_mass, curent_dir, curent_speed = fireballs.pop(0)
        # 1번 - N번 행이 연결되어 있기 떄문에
        next_row = (curent_row + curent_speed * dr[curent_dir]) % N
        next_col = (curent_col + curent_speed * dc[curent_dir]) % N
        # 리스트 이기에, 해당 값(row, col)에 여러개의 파이어볼들이 append로 들어갈 수 있음
        # 싸움땅에서도 같은 테크닉이 이렇게 쓰임
        MAP[next_row][next_col].append([curent_mass, curent_speed, curent_dir])


    #2 파이어볼 이동후 행동

    #2개 이상인지 체크
    for r in range(N):
        for c in range(N):
            #2개 이상인 경우 => 4개의 파이어볼로 쪼개기
            if len(MAP[r][c]) > 1:

                #초기 데이터 값
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])

                #모인 파이어볼 들 중에서 값을 하나씩 꺼내면서 본다.
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

                #모인 질량이 값이 있을 경우, 모여진 파이어볼을 4방향으로 이동시킴
                if sum_m // 5:
                    for d in nd:
                        fireballs.append([r, c, sum_m // 5, sum_s // cnt, d])

            # 1개인 경우
            # 액션을 취할 떄도, 내가 가지고 있는 data 구조를 잘 파악 했기에 쉽게 한번에 할 수 있음.
            # fireballs => fireballs.append([r-1, c-1, m, s, d])
            # MAP       => MAP[next_row][next_col].append([curent_mass, curent_speed, curent_dir])
            # 따라서, 현재 좌표(r,c)에는 파이어볼이 1개라, 기존의 자신 것을 그대로 가지고 오는 행위
            if len(MAP[r][c]) == 1:
                fireballs.append([r, c] + MAP[r][c].pop())

print(sum([f[2] for f in fireballs]))
#
# N, M, K = map(int, input().split())
# fireballs = []
# for _ in range(M):
#     _r, _c, _m, _s, _d = list(map(int, input().split()))
#     fireballs.append([_r-1, _c-1, _m, _s, _d])
#
# MAP = [[[] for _ in range(N)] for _ in range(N)]
#
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
# for _ in range(K):
#     # 파이어볼 이동
#     while fireballs:
#         cr, cc, cm, cs, cd = fireballs.pop(0)
#         nr = (cr + cs * dx[cd]) % N  # 1번-N번 행 연결되어있기 때문
#         nc = (cc + cs * dy[cd]) % N
#         MAP[nr][nc].append([cm, cs, cd])
#
#     # 2개 이상인지 체크
#     for r in range(N):
#         for c in range(N):
#             # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
#             if len(MAP[r][c]) > 1:
#                 sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])
#                 while MAP[r][c]:
#                     _m, _s, _d = MAP[r][c].pop(0)
#                     sum_m += _m
#                     sum_s += _s
#                     if _d % 2:
#                         cnt_odd += 1
#                     else:
#                         cnt_even += 1
#                 if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
#                     nd = [0, 2, 4, 6]
#                 else:
#                     nd = [1, 3, 5, 7]
#                 if sum_m//5:  # 질량 0이면 소멸
#                     for d in nd:
#                         fireballs.append([r, c, sum_m//5, sum_s//cnt, d])
#
#             # 1개인 경우
#             if len(MAP[r][c]) == 1:
#                 fireballs.append([r, c] + MAP[r][c].pop())
#
# print(sum([f[2] for f in fireballs]))
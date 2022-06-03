'''

게임에서 얻을 수 있는 점수의 최댓값을 구하여라!

게임판위에서 출발 위치와 진행 방향을 임의로 선정가능 하다,,!

방향 바꾸는 거 이해하는데 오래 걸림,, 나 구현 어려워하네,, 삼성풀이 주간에 최대한 풀어보려고 해보고,,! 손에 익히게 하자!

'''


# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


#블록별 방향 바꾸기
# 1번 블록을 0번방향에서 왔을때(오른쪽에서) 방향 바뀌는 방향 2(왼쪽)으로 간다!

change_dir = ((),
              (2, 0, 3, 1),
              (2, 3, 1, 0),
              (1, 3, 0, 2),
              (3, 2, 0, 1),
              (2, 3, 0, 1))


#게임 시작 위치와 방향 넘기면 게임 점수 리턴
def play_game(row, col, dir):
    #처음 좌표를 기억해두기!
    now_row = row
    now_col = col
    score = 0

    while True:
        #여기서 바뀐 dir이 들어가면서 좌표가 이동이 되는구먼! 한칸씩!
        row += dr[dir]
        col += dc[dir]
        if not (0 <= row < N and 0 <= col < N): #범위 밖에 있으면 장외!
            dir = (dir + 2) % 4 # 2칸 이동하면! 반대 방향인데! %4를 함으로서! 사방향의 인덱서의 범위를 벗어나지 않을 수 잇다! 원형을 만드는거지!
            score += 1

        #범위 안에서 이동!
        else:
            #처음 좌표로 다시 돌아오고! 블랙홀에 도착하면 게임 끝
            if (row, col) == (now_row, now_col) or MAP[row][col] == -1 :
                break
            #1 ~ 5 벽돌 만나서 방향 전환
            elif 1 <= MAP[row][col] <= 5:
                dir = change_dir[MAP[row][col]][dir]
                score += 1
            #웜홀을 만남
            elif 6 <= MAP[row][col] <= 10:
                #바로 좌표 바꿔주기!
                row, col = gate[(row, col)]
    global maxScore
    if score > maxScore: #최대값 갱신해주기
        maxScore = score

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    tmp = {}
    gate = {}
    
    MAP = [list(map(int, input().split())) for _ in range(N)] #맵 입력받기 
    
    for row in range(N):
        for col in range(N):
            if 6 <= MAP[row][col] <= 10: #웜홀 만남
                if MAP[row][col] in tmp: #같은 번호의 웜홀을 만나고 또 만남!
                    gate[tmp[MAP[row][col]]] = (row, col)
                    #반대로도 넣는다,,! why?! 밑에서도 두 공간 모두에서 웜홀 이동을 해야 한다!
                    gate[(row, col)] = tmp[MAP[row][col]]

                else:
                    tmp[MAP[row][col]] = (row, col)
    # key =  (row, col) / value = (row, col) => 같은 번호의 웜홀 번호 좌표끼리 key - value로 연결
    # print(gate)
    # for i in range(1, N + 1): #A맨 바깥 둘레 제외하고 채워야 하니깐
    maxScore = - 1

    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 0:
                #빈공간에서 4방향 탐색!
                for dir in range(4):
                    play_game(row, col, dir)

    print('#%d' % tc, end=' ')
    if maxScore == -1:
        print(0)
    else:
        print(maxScore)

# 이런 풀이도 존재! 일단 맵을 다 둘러싸기! 그리고 MAX를 이용해서!(return이 숫자)
'''
# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 블록별 방향 바꾸기
change_dir = ((),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 0, 3, 2))

# 게임 시작 위치와 방향 넘기면 게임 횟수 리턴
def play_game(r, c, d):
    global wormhole_info
    score = 0
    sr, sc = r, c       # 시작 위치 저장
    while True:
        r += dr[d]      # 이동하면서 시작해야 함
        c += dc[d]
        # 출발 위치로 돌아오거나 블랙홀 만나면 게임 끝. 점수 리턴
        if (r, c) == (sr, sc) or A[r][c] == -1:
            return score
        if 1 <= A[r][c] <= 5:           # 블록 만나면 방향 바꾸고 점수 + 1
            d = change_dir[A[r][c]][d]
            score += 1
        elif 6 <= A[r][c] <= 10:        # 웜홀 만나면 같은 번호의 웜홀로 이동. 방향은 유지
            r, c = wormhole_info[(r, c)]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    wormhole_check = [0] * 11
    wormhole_info = dict()      # 웜홀 쌍 정보
    A = [[5] * (N+2)]   # 맵 벽(5)으로 둘러싸기
    for i in range(1, N+1):
        A.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, N+1):
            if 6 <= A[i][j] <= 10:
                num = A[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:   # 같은 번호 웜홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    A.append([5] * (N+2))

    # 게임 시작
    MAX = float('-inf')  # 게임에서 얻을 수 있는 최대 점수
    for sr in range(1, N+1):
        for sc in range(1, N+1):
            if A[sr][sc] == 0:      # 시작 위치와 방향 정한 후 게임 start
                for sd in range(4):
                    MAX = max(MAX, play_game(sr, sc, sd))
    print("#{} {}".format(tc+1, MAX))


'''

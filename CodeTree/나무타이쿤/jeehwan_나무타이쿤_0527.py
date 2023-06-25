'''


1. 영양제 이동

2. 이동 후 1씩 증가

3. 대각선 1이상 체크 후, 그 수 만큼 값 증가.

4. 높이 2 이상 잘라내고, 해당 위치가 바로 다시 영양제가 있는 곳으로 기록 (영양제 있던 곳은 그 다음 영양제 위치가 될 수 없음)
    => 영양제 위치 다시 기록


영양제의 위치가 중요하니, 해당 위치를 기록하는 배열 / visited 만들기.

yyz = [(row1, col1), (row, col2)] 영양제 배열이 존재하는 위치 기록

yyz_visited = [[Fasle] * n for _ in range(n)]



첫번째 줄에는 격자의 크기 n, 리브로수를 키우는 총 년 수 m이 주어집니다.

이후 두번째 줄부터 n+1번째 줄까지 서로 다른 리브로수의 높이가 주어집니다.

이후 m개의 줄에는 각 년도의 이동 규칙이 주어집니다.

이동 규칙은 이동 방향 d, 이동 칸 수 p로 주어지고, d는 1번부터 8번까지 각각 → ↗ ↑ ↖ ← ↙ ↓ ↘으로 주어집니다.

3 ≤ n ≤ 15

1 ≤ m ≤ 100

0 ≤ 초기에 주어지는 리브로수의 높이 ≤ 100

1 ≤ d ≤ 8

1 ≤ p ≤ min(n, 10)


입력

5 1
1 0 0 4 2
2 1 3 2 1
0 0 0 2 5
1 0 0 0 3
1 2 1 3 3
1 3

'''

import copy

#대각선 체크
dr_dia = [-1, 1, -1, 1]
dc_dia = [-1, -1, 1, 1]

#8방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

#초기 입력

n, m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

#굳이 여기서 받아서 할 필요x, 이중 for문을 만들고 싶지 않아.
# ORDER = []
#
# for _ in range(m):
#     d, p = map(int, input().split())
#     ORDER.append((d, p))

#print(MAP, ORDER)

#영양제 좌표 기록, (초기 영양제의 위치는  n x n 격자의 좌하단의 4개의 칸)
yyz = []

#영양제 기록배열
yyz_visited = [[False] * n for _ in range(n)]

#문제 잙 읽기  // 변수명 귀찮아도 길게,,,! 헷갈리지 않게,, 디버깅하기 쉽게
for row in range(n - 2, n):
    for col in range(2):
        yyz_visited[row][col] = True


def stepOneAndTwo(dir, power):

    #이동을 위한 임시배열 생성
    global yyz_visited, yyz
    #다음번 반복을 위한 초기화
    tempVisted = [[False] * n for _ in range(n)]
    yyz = []

    # n = len(yyz)
    # #dir 방향으로, power만큼 이동 후 1씩 증가
    # for row, col in yyz[:]:
    #
    #     next_row = (n + row + dr[dir] * power) % n
    #     next_col = (n + col + dc[dir] * power) % n
    #     tempMAP[next_row][next_col] += 1
    #     yyz.append((next_row, next_col))
    #     #print(next_row, next_col)

    for row in range(n) :
        for col in range(n):
            if yyz_visited[row][col]:
                next_row = (n + row + dr[dir] * power) % n
                next_col = (n + col + dc[dir] * power) % n
                tempVisted[next_row][next_col] = True
                MAP[next_row][next_col] += 1
                yyz.append((next_row, next_col))


    yyz_visited = copy.deepcopy(tempVisted)

def stepThree():


    #영양제가 있는 위치, 대각선 체크
    for row, col in yyz :
        for dir in range(4):

            next_row = row + dr_dia[dir]
            next_col = col + dc_dia[dir]

            if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] >= 1:
                MAP[row][col] += 1


def stepFour():


    global yyz_visited

    temp_yyz_visited = [[False] *  n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if MAP[row][col] >= 2 and not yyz_visited[row][col]:
                temp_yyz_visited[row][col] = True
                MAP[row][col] -= 2


    yyz_visited = copy.deepcopy(temp_yyz_visited)


#시물레이션
for _ in range(m):

    d, p = map(int, input().split())

    stepOneAndTwo(d - 1, p)

    stepThree()

    stepFour()

    debug = 1


ans = 0
for row in range(n):
    for col in range(n):
        ans += MAP[row][col]

print(ans)










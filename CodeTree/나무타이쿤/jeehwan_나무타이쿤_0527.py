'''


1. 영양제 이동

2. 이동 후 1씩 증가

3. 대각선 1이상 체크 후, 그 수 만큼 값 증가.

4. 높이 2 이상 잘라내고, 해당 위치가 바로 다시 영양제가 있는 곳으로 기록
    => 영양제 위치 다시 기록


영양제의 위치가 중요하니, 해당 위치를 기록하는 배열 만들기.


yyz = [(row1, col1), (row, col2)] 영양제 배열이 존재하는 위치 기록


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

for row in range(n - 2, n):
    for col in range(2):
        yyz.append((row, col))

#print(yyz)


def stepOneAndTwo(dir, power):

    #이동을 위한 임시배열 생성
    tempMAP = copy.deepcopy(MAP)

    #dir 방향으로, power만큼 이동 후 1씩 증가
    for row, col in yyz:

        next_row = (n + row + dr[dir]) % n
        next_col = (m + col + dc[dir] ) % m
        tempMAP[next_row][next_col] += 1

    #복사
    for row in range(N):
        for col in range(N):
            MAP[row][col] = tempMAP[row][col]





def stepThree():

    tempMAP = copy.deepcopy(MAP)

    #대각선 체크 후

#시물레이션

for _ in range(m):

    d, p = map(int, input().split())

    stepOne(d, p)

    #stepTwo()

    #stepThree()

    #stepFour()









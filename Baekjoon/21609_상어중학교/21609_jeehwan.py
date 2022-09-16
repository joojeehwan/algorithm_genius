'''

상어 중학교

문제 이해


최대 N이 20인 N * N 의 이차원 배열의 각 칸에 블록 번호가 입력됩니다.
검은 블록은 -1, 무지개 블록은 0, 일반 블록은 1 ~ 5까지
무지개 블록은 어떤 숫자의 일반 블록으로 변화 가능
규칙에 따라 게임을 진행 -> 얻을 수 있는 점수를 출력

(1) 크기가 가장 큰 블록을 찾는다 -> 그러한 블록이 여러개 라면, 무지개 블록의 수가 많은 블록 그룹, 기준 불록의 행이 가장 큰 것, 열이 가장 큰 것.

(2) 1에서 찾은 블록 그룹의 모든 블록을 제거 -> 제거된 점수의 갯수 만큼 제곱해서

(3) 격자에 중력이 적용 (검은 블록 적용x)

(4) 격자가 90도 반 시계 방향 회전

(5) 다시 격자에 중력이 적용 (검은 블록 적용x)


문제 해결 방식

-  bfs를 이용해서, 가장 큰 블록 그룹을 찾는다.

-  가장 큰 블록을 제거하고, 점수를 계산

-  중력작용을 구현

-  반시계 방향으로 90도 회전

'''




from collections import deque


#기본 입력받기
n, m  = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

#델타 배열
#반 시계방향 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

#1. 가장 큰 블록 그룹을 찾고, 삭제되는 불록들의 좌표를 기억하고,
#2. 블록 그릅을 제거 하고
#3. 점수 까지 계산
def calcPoint() :
    #점수
    point = 0
    #가장 큰 블록 그룹의 좌표를 저장
    max_area = []
    #가장 큰 무지개 블록
    max_rainbow = 0

    for color in range(1, m+1):
        #안엔다가 두는 이유. => 무지개 블록이 없다면 밖에 두어도 됨. 왜냐면 색깔이 다른 블록끼리는 겹칠일이 없다.
        #문제는 무지개 블록 다른 색깔의 블록을 밝을 수 있어서. 초기화를 해주어야 한다.
        visited = [[False] * 20 for _ in range(20)]
        for row in range(n):
            for col in range(n):
                #방문이 가능한지 체크 & 내가 보고 검색하고자 하는 색깔이 맞으면,
                if not visited[row][col] and MAP[row][col] == color:

                    #bfs 탐색을 해보자
                    q = deque()
                    q.append([row, col])
                    result_lst = [[row, col]]
                    rainbow = 0
                    visited[row][col] = True

                    while q:
                        now_row, now_col = q.popleft()
                        #4방향 탐색
                        for dir in range(4):
                            next_row = now_row + dr[dir]
                            next_col = now_col + dc[dir]

                            #if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                            #      #같은 방향끼리 숫자 카운팅
                            #     if MAP[next_row][next_col] == color:
                            #         visited[next_row][next_col] = True
                            #         q.append([next_row, next_col])
                            #         point += 1
                            #         result_lst.append([next_row, next_col])
                            #
                            #     elif MAP[next_row][next_col] == 0:
                            #         visited[next_row][next_col] = True
                            #         q.append(([next_row, next_col]))
                            #         point += 1
                            #         result_lst.append([next_row, next_col])
                            #         rainbow += 1

                            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                                continue
                            #범위 체크 & 방문하지 않은 곳.
                            if  not visited[next_row][next_col] and (MAP[next_row][next_col] == color or MAP[next_row][next_col] == 0):

                                q.append([next_row, next_col])
                                visited[next_row][next_col] = True
                                result_lst.append([next_row, next_col])
                                point += 1
                                if MAP[next_row][next_col] == 0 :
                                    rainbow += 1
                        # 가장 많이 인접해 있는, 숫자를 가지는 것을 기록하기 위함.
                        # 3가지 case 존재 모두 나열
                    if len(max_area) < len(result_lst) or (len(max_area) == len(result_lst) and max_rainbow < rainbow) or (len(max_area) == len(result_lst) and max_rainbow == rainbow and max_area[0] < result_lst[0]):
                        max_area = result_lst[:]
                        max_rainbow = rainbow

        #2개 이상이 되지 않는 것은 counting 하지 않는다.
    if len(max_area) >= 2:
        point = len(max_area) * len(max_area)
        #블록 제거
        for row , col in max_area:
            MAP[row][col] = -2
    return point

def gravity() :
    global MAP
    for col in range(n):
        #열마다 갱신하기 때문에 이곳에 위치
        blank = 0
        #아래에서 위로 올라가야해
        for row in range(n-1, -1, -1):
            if MAP[row][col] == -2:
                blank += 1
            #검은색을 만나면 다시 초기화 하고 다시 세야대! 중력의 영향을 받지 않아.
            elif MAP[row][col] == -1:
                blank = 0

            #이제 옮기자!
            else:
                #이 조건이 필요하다.
                if blank != 0 :
                    MAP[row + blank][col] = MAP[row][col]
                    MAP[row][col] = -2


def rotate() :
    global MAP
    temp = [[0] * n for _ in range(n)]
    #90도로 돌리는 것 반시계 방향으로 돌리는 것.
    for i in range(n):
        for j in range(n):
            temp[n - 1 - j][i] = MAP[i][j]

    #원형에 복사하기
    MAP = temp[:]


point = 0
curPoint = 0
while True :
    curPoint = calcPoint()
    point += curPoint
    gravity()
    rotate()
    gravity()
    if curPoint != 0 :
        continue
    break

print(point)








data = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]

data.sort(key=lambda x : (x[1], x[0]))

print(data)

from collections import deque


#델타 배열도 정해져 있음. 좌 하 우 상 -> 내가 그리고 싶은 나선형의 모양대로
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


n = 5

MAP = [[0] * n for _ in range(n)]
print(MAP)
def solve(row, col) :

    visited = [[False] * n for _ in range(n)]
    dir = -1 # 아무 방향이x
    while True:

        if row == 0 and col == 0 :
            break

        visited[row][col] = True
        # 이 위치가 중요
        next_dir = (dir + 1) % 4
        next_row = row + dr[next_dir]
        next_col = col + dc[next_dir]
        
        #방문 했으면, 방향을 바꾸지 않고, 현재 방향을 유지 한채 그대로 이동
        if visited[next_row][next_col] :
            next_dir = dir
            next_row = row + dr[next_dir]
            next_col = col + dc[next_dir]
            MAP[next_row][next_col] = 1
        debug = 1
        row, col, dir = next_row, next_col, next_dir
        MAP[next_row][next_col] = 1

solve(n // 2, n // 2)
print(MAP)



MAP = [[[] for _ in range(3)] for _ in range(3)]


print(MAP)

# 격자 회전


# 회전

MAP = [[1,2,3,4,5],
       [6, 7, 8, 9, 10],
       [11,12,13,14,15],
       [16,17,18,19,20],
       [21,22,23,24,25]]

n = 5

temp = [[0] * n for _ in range(n)]


def rotate_square(start_row, start_col, square_n):

   for row in range(start_row, start_row + square_n) :
       for col in range(start_col, start_col + square_n):

            #(0, 0)으로 가져와서 변환 진행
            o_row, o_col = row - start_row, col - start_col

            #좌표 변환 (회전)
            r_row = o_col
            r_col = square_n - o_row - 1

            #다시 원래 좌표 위치로
            temp[r_row + start_row][r_col + start_col] = MAP[row][col]

sqaure_n = n // 2
rotate_square(0, 0, sqaure_n)
rotate_square(0, sqaure_n + 1, sqaure_n)
rotate_square(sqaure_n + 1, 0, sqaure_n)
rotate_square(sqaure_n + 1, sqaure_n + 1, sqaure_n)
print(temp)





MAP = [[i for i in range(8)] for _ in range(8)]

n = 8

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

temp = [[0] * n for _ in range(n)]
# 2^l 크기의 격자를 선택해서 들어왔다.
# 2^(l-1) 크기로 4등분된 빙하를 한 덩이씩 보면서 회전하는 함수
# d(방향) 에 맞춰 옮겨준다.
def rotating(sr, sc, half, d):
    for r in range(sr, sr+half):
        for c in range(sc, sc+half):
            nr = r + dr[d] * half
            nc = c + dc[d] * half
            temp[nr][nc] = MAP[r][c]


# 빙하를 선택하는 함수
# 2^N * 2^N의 빙하를 2^l * 2^l 만큼씩 선택한다.
# 그 안에서 2^(l-1) * 2^(l-1) 만큼씩 반시계 90'로 회전한다.
def iceberg_rotate(level):
    if level == 0:
        return
    l_len = 2 ** level
    h_len = l_len // 2

    # 4등분으로 반시계 방향으로 90' 회전하지만, 꼭 회전공식을 사용하지 않아도 된다.
    # 좌상, 우상, 우하, 좌하 격자 순대로 우 -> 하 -> 좌 -> 상의 방향으로 격자를 옮기는 것과 같은 행위다.
    # 이 생각을 떠올리긴 했지만, 4경우 모두 하나의 for 반복문 내에서 처리하려고 한 점이 더 돌아가게 만들었다.

    # length가 전체 격자의 길이,
    # 그 중에서 l_len만큼 잡아서, 그 안에 h_len만큼 회전
    for start_r in range(0, 8, l_len):
        for start_c in range(0, 8, l_len):
            rotating(start_r, start_c, h_len, 0)
            rotating(start_r, start_c + h_len, h_len, 1)
            rotating(start_r+h_len, start_c+h_len, h_len, 2)
            rotating(start_r+h_len, start_c, h_len, 3)

    # 회전 사항 반영
    for r in range(8):
        MAP[r] = temp[r][:]
        temp[r] = [0] * 8
print(MAP)
iceberg_rotate(2)
print(MAP)

length = 8

def rotating(sr, sc, length, dir):
    for r in range(sr, sr + length):
        for c in range(sc, sc + length):
            nr = r + dr[dir] * length
            nc = c + dc[dir] * length
            temp[nr][nc] = MAP[r][c]

def iceberg_rotate(level) :
    if level == 0:
        return

    entire_range_len = 2 ** level
    rotate_len = entire_range_len // 2


    for start_r in range(0, length, entire_range_len):
        for start_c in range(0, length, entire_range_len):
            rotating(start_r, start_c, rotate_len, 0)
            rotating(start_r, start_c + rotate_len, rotate_len, 1)
            rotating(start_r + rotate_len, start_c + rotate_len, rotate_len, 2)
            rotating(start_r + rotate_len, start_c, rotate_len, 3)




grid = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(5)]

grid2 = [[[] for _ in range(5)] for _ in range(5)]


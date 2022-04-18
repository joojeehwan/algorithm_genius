"""
백준 아이디 jongsun1993의 답안 참고
https://www.acmicpc.net/source/41714775
PyPy3로 시간이 무려 938ms만 나옴
내가 푼 코드랑 변수 명을 일치시켜봄
"""

# sys 입력으로 입력 시간 단축
import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]

empty_list = []  # 0의 자리(row, col)를 담는 배열
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            empty_list.append((row, col))

empty_cnt = len(empty_list)  # 0의 개수
answer = 0
# 나는 row, col, 3*3 기준으로 이미 있는 값들을 미리 저장해두면 더 빠를 것이라 생각했다.
# 하지만 배열을 생성하고 매번 값을 바꾸는 과정이 사실을 쓸모 없었고
# 이 또한 시간을 잡아먹는 이유가 아니었을까 싶다.


def dfs(count, sudoku):
    global answer

    if count == empty_cnt:
        answer = sudoku
        # return 1을 하는 이유는 찾았을 경우 0으로 원복하는 코드를 막기 위해서이다.
        return 1

    now_row, now_col = empty_list[count]
    # 10개인 이유는 숫자 그대로를 쓰고싶기 때문이다.
    possible = [1] * 10

    # 지금 행 기준으로 이미 있는 숫자들은 possible 배열의 값을 0으로 처리한다.
    for num in sudoku[now_row]:
        possible[num] = 0
    # 지금 열 기준으로 이미 있는 숫자들은 ~~
    for row in range(9):
        possible[sudoku[row][now_col]] = 0
    # 지금 3 * 3 칸 기준으로 이미 있는 ~~
    now_x, now_y = 3*(now_row//3), 3*(now_col//3)
    for dx in range(3):
        for dy in range(3):
            possible[sudoku[now_x+dx][now_y+dy]] = 0

    # 이제 possible 배열에서 1값을 가진 숫자만 활용할 수 있다.
    # 아마 나는 가능한 숫자를 만드는 과정이 더 복잡했던게 문제가 아닐까 싶다.
    for number in range(1, 10):
        if possible[number]:
            sudoku[now_row][now_col] = number
            if dfs(count+1, sudoku):
                return 1
            sudoku[now_row][now_col] = 0
    return 0


dfs(0, sudoku)

for line in ans:
    print(*line)
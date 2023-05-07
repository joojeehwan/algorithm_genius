'''


- 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동

- 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 됨

- 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.


이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다.

보드의 크기와 보드판의 블록 상태가 주어졌을 때,

최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.


완전 탐색

'''

import copy


def left(temp_MAP):
    pass


def right(temp_MAP):
    pass


def up(temp_MAP):
    pass


def down(temp_MAP):
    pass


def dfs(dfs_MAP, lev) :

    global ans

    #base 조건
    if lev == 5 :
        for row in range(N):
            for col in range(N) :
                ans = max(ans, MAP[row][col])

        return

    #재귀
    else:
        for i in range(4):  # "좌 우 상 하" 이동

            temp_MAP = copy.deepcopy(dfs_MAP)

            if i == 0: #상

                dfs(left(temp_MAP), lev + 1)

            elif i == 1 :

                dfs(right(temp_MAP), lev + 1)

            elif i == 2 :
                dfs(up(temp_MAP), lev + 1)

            else:
                dfs(down(temp_MAP), lev + 1)

N = int(input())

MAP = [list(map(int, input().split(()))) for _ in range(N)]

ans = 0



#확인할 것.

import sys
from copy import deepcopy
input = sys.stdin.readline

# INPUT
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# UP
def up(board):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer += 1
                    board[pointer][j] = tmp
    return board

# DOWN
def down(board):
    for j in range(n):
        pointer = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

# LEFT
def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer]= tmp
    return board

# RIGHT
def right(board):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board


# DFS
def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return max(map(max, board))

    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야 한다.
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))

print(dfs(board, 0))




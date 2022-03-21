import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# 각 체크 함수의 로직
# 다음 조건을 만족하는 한 정해진 방향으로 계속 가며 돌을 체크한다.
#     바둑판을 벗어나지 않는다.
#     다른 돌을 마주친다.
#     5개가 넘는 연속된 돌을 본다.
# 이동을 멈췄을 때 만난 돌이 정확히 다섯개인 경우 다음 조건을 판단
#     시작 돌이 테두리이거나 시작 돌 이전으로 연속이 이어지지 않는 경우 참 반환
# 그 외의 경우 거짓 반환

def horizontalCheck(r, c, n):
    start = r
    chain = 0
    while r < 19 and board[r][c] == n and chain <= 5:
        chain += 1
        r += 1
    if chain == 5:
        if start == 0 or board[start-1][c] != n:
            return True
    return False

def diagonalCheckDR(r, c, n):
    sr = r
    sc = c
    chain = 0
    while r < 19 and c < 19 and board[r][c] == n and chain <= 5:
        chain += 1
        r += 1
        c += 1
    if chain == 5:
        if sr == 0 or sc == 0 or board[sr-1][sc-1] != n:
            return True
    return False

def verticalCheck(r, c, n):
    start = c
    chain = 0
    while c < 19 and board[r][c] == n and chain <= 5:
        chain += 1
        c += 1
    if chain == 5:
        if start == 0 or board[r][start-1] != n:
            return True
    return False

def diagonalCheckUR(r, c, n):
    sr = r
    sc = c
    chain = 0
    while r >= 0 and c < 19 and board[r][c] == n and chain <= 5:
        chain += 1
        r -= 1
        c += 1
    if chain == 5:
        if sr == 18 or sc == 0 or board[sr+1][sc-1] != n:
            return True
    return False

winner = 0
wr = ''
wc = ''

for r in range(19):
    for c in range(19):
        if board[r][c] != 0:
            result = False
            result = result or horizontalCheck(r, c, board[r][c])
            result = result or diagonalCheckDR(r, c, board[r][c])
            result = result or verticalCheck(r, c, board[r][c])
            result = result or diagonalCheckUR(r, c, board[r][c])
            if result:                
                winner = board[r][c]
                wr = str(r + 1)
                wc = str(c + 1)
                break
    if winner:
        break

print(winner)
if winner:
    print(wr + ' ' + wc)
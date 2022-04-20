import sys
N = int(sys.stdin.readline())
MAP = [0] * N  # 0번 행의 열 위치, 1번 행의 열 위치 ...
answer = 0


def check(row):
    # 현재 row의 윗 줄들과 보면서 비교하는 것
    for i in range(row):
        # row번째 행에 위치한 퀸의 col 값과 다른 행에 위치한 퀸의 열 값이 같거나,
        # (열 - 열 == 행 - 행) 이면 같은 대각선에 있다는 점을 이용해 푼다.
        # (행 - 행 == 열 - 열)이면 같은 대각선이라는 점은 어떻게 떠올린걸까...
        if MAP[row] == MAP[i] or abs(MAP[row] - MAP[i]) == row - i:
            return False
    return True


def dfs(count):
    global answer
    if count == N:
        answer += 1
        return
    for col in range(N):
        MAP[count] = col  # 이 자리로 찜하고
        if check(count):  # 그 자리에 갈 수 있겠니?
            dfs(count+1)  # 된다면 아랫 줄로 내려가보자.


dfs(0)
print(answer)
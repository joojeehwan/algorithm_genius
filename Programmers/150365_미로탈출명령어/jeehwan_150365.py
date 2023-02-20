#dfs 풀이
# 참고
# https://velog.io/@chocochip/2023-KAKAO-BLIND-RECRUITMENT-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%92%80%EC%9D%B4
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

#미리 사전순으로 검색하기 위함. => d l r u 순으로 탐색을 시작해야, 나머지 경우에 대해서 방문하지 않고, 탈출 경로를 찾을 수 있음.
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
Alpha = ['d', 'l', 'r', 'u']
answer = "z"

#범위체크
def isVaild(nx, ny, n, m):
    return 1 <= nx and nx <= n and 1 <= ny and ny <= m


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):
        return
    if x == r and y == c and cnt == k:
        answer = prev_s
        return
    for i in range(4):
        if isVaild(x + dx[i], y + dy[i], n, m) and prev_s < answer: #대소 비교만으로 사전순 체크가 가능한.. 파이썬..사랑한다...
            dfs(n, m, x + dx[i], y + dy[i], r, c, prev_s+Alpha[i], cnt + 1, k)


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    #탈출 지점 도착후에, 두번이동 하면 다시 제자리로 돌아올 수 있다. 홀수면 다시 못들어온다.
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)

    return answer



#참고1. bfs풀이


from collections import deque

def get_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def solution(n, m, x, y, r, c, k):
    #이거 왜 해..?!

    x, y = y - 1, x - 1
    r, c = r - 1, c - 1

    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]

    path_map = {
        0: "d",
        1: "l",
        2: "r",
        3: "u",
    }

    diff = k
    answer = ""
    while diff:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if get_dist(nx, ny, c, r) <= diff:
                answer += path_map[i]
                x, y = nx, ny
                diff -= 1
                break
        else:
            break

    if len(answer) == k and x == c and y == r:
        return answer
    return "impossible"



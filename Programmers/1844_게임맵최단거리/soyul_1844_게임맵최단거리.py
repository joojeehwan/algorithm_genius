def solution(maps):

    n = len(maps)
    m = len(maps[0])

    # bfs로 거리를 map에 기록해줌
    def bfs(maps):

        di = [0, 0, -1, 1]
        dj = [1, -1, 0, 0]

        q = []
        q.append((0, 0))
        maps[0][0] = 0

        while q:
            now_i, now_j = q.pop(0)

            for k in range(4):
                next_i = now_i + di[k]
                next_j = now_j + dj[k]

                if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                    continue
                if maps[next_i][next_j] != 1:
                    continue

                maps[next_i][next_j] = maps[now_i][now_j] - 1           # visited 배열을 쓰지 않으려고 -1씩 기록 후 마지막에 절대값 출력
                q.append((next_i, next_j))

        return maps[n-1][m-1]

    answer = bfs(maps)
    if answer == 1:
        return -1
    else:
        return abs(answer) + 1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
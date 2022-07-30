''''


1. 국경선을 열지 말지?! 를 결정 (문제에 주어진 조건)

=> bfs/dsf를 사용해서

2. 국경선을 열었다면 조건에 맞게 인구이동 시작

3. 1 -2 번을 더이상의 인구이동이 없을떄까지 반복


temp배열을 만들어서, 국경선 공유하고 있는 나라들의 좌표값 넣기!

flag 1 => 인구 이동 시작 => 국경선 공유 하고 있는 모든 나라들의 합에서 국경을 공유하고 있는 나라들의 개수로 나눔!
그리고 그 값을 temp에 있는(좌표)나라들의 인구로 교체!
flag 0 => 인구 이동 끝 => while문 종료

'''


from collections import deque

#초기 입력
N, L, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

#벡터 배열 상, 하, 좌, 우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    q = deque()
    temp = [] #국경선을 공유 하고 있는 나라들의 좌표가 담김
    q.append((row, col))
    temp.append((row, col))
    
    #q가 빌때까지
    while q:
        row, col = q.popleft()
        #4방향 모두 탐색
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            
            #범위 체크 + 한번도 안간 곳
            if 0<= next_row < N and 0 <= next_col < N and visited[next_row][next_col] == 0:
                #국경선 오픈 조건! 인구수 비교 로직
                if L <= abs(MAP[next_row][next_col] - MAP[row][col]) <= R:
                    visited[next_row][next_col] = 1
                    q.append((next_row, next_col))
                    temp.append((next_row, next_col))

    return temp
        
answer = 0
while True:
    visited = [[0] * (N) for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            #한번도 가지 않은 곳
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                #국경 열리고! 인구 이동 시작

                if len(country) > 1:

                    flag = 1
                    numberOfCountry = 0
                    for row, col in country:
                        numberOfCountry += MAP[row][col]

                    processNumber = numberOfCountry // len(country)
                    # 오 멋지네,, 파이썬스럽네
                    # number = sum([graph[x][y] for x, y in country]) // len(country)

                    for row, col in country:
                        MAP[row][col] = processNumber

    if flag == 0:
        break
    answer += 1
print(answer)


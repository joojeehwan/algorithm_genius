'''
최초에 방문했던 시간에서 2초뒤에 다시 재방문

=> 위치 x에서 +1 과 -1 을 번갈아가면서, 방문하기 떄문

따라서 주어진 T초에 위치 X를 방문했는지 알기 위해서는,

위치 X를 방문한 짝수 최소 시간과 홀수 최소 시간만 알고 있으면 된다.



동적변수로 리스트 만들기 .. 어렵다

'''


from collections import deque

MAX_NUM = 500000

N, K = map(int, input().split())

visited = [[-1 for _ in range(MAX_NUM + 1)] for _ in range(2)]

# visited[0][n] : 홀수 시간에 위치 n을 방문한 최소 시간
# visited[1][n] : 짝수 시간에 위치 n을 방문한 최소 시간
def bfs() :

    #1. 큐 생성
    q = deque()

    #2. 초기값 세팅
    q.append((N, 0)) #노드 번호(n), 몇번 만에 해당 노드에 접근 했는지(cnt)
    # 당연히 시작값(수빈)이니 0으로 접근 가능

    #3.visited 배열 할당
    visited[0][N] = 0


    #4. queue 돌기

    while q:

        n, cnt = q.popleft()

        #cnt의 홀짝 여부 결정
        flag = cnt % 2

        for next_node in [n+1, n-1, 2*n] :
            if 0 <= next_node <= MAX_NUM and visited[1-flag][next_node] == -1 :
                visited[1-flag][next_node] = cnt + 1
                q.append((next_node, cnt + 1))


bfs()

t = 0
flag = 0
res = -1

while K <= MAX_NUM :
    if visited[flag][K] != -1:
        if visited[flag][K] <= t:
            res = t
            break

    flag = 1 - flag
    t += 1
    K += t

print(res)
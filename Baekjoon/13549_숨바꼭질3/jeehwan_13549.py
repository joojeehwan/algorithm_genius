

'''


- 수빈이는 현재 N에 있고, 동생은 K에 있다.

- 수빈이는 걷거나, 순간이동 가능

    - 걷을 때, 1초 후에, x - 1 Ehsms x + 1
    - 순간이동, 0초 헤에, 2**X

수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하라


sol) 순간 이동과 걷기의 시간(가중치)가 다르므로, 큐 2개로 나뉘어 구현하며 되는데

python의 deque 자체가 양방향 이므로, 이를 이용

순간이동 appendleft // 걷는 경우 append
'''
from collections import deque



N, K = map(int, input().split())


visited = [False] * int(10e6)

print(visited)


'''


- 수빈이는 현재 N에 있고, 동생은 K에 있다.

- 수빈이는 걷거나, 순간이동 가능

    - 걷을 때, 1초 후에, x - 1 Ehsms x + 1
    - 순간이동, 0초 헤에, 2**X

수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하라


sol) 순간 이동과 걷기의 시간(가중치)가 다르므로, 큐 2개로 나뉘어 구현하며 되는데

python의 deque 자체가 양방향 이므로, 이를 이용

순간이동 appendleft // 걷는 경우 append
'''

# bfs 풀이
from collections import deque



N, K = map(int, input().split())

visited = [0] * int(10e6)

q = deque()
q.append((N))
visited[N] = True

while q:

    now_node = q.popleft()

    if now_node == K:
        print(visited[now_node])

    else:

        for next_node in (2*now_node, now_node - 1, now_node + 1):

            # 이동 후에 반드시 범위 체크 & 한번도 방문하지 않은 곳
            if 0 <= next_node < 100001 and visited[next_node] :
                #순간이동
                if next_node == 2 * now_node:
                    #visited 배열에 값을 활용해 가중치를 표현
                    visited[next_node] = visited[now_node]
                    q.appendleft((next_node))
                # 걸어서
                else:
                    visited[next_node] = visited[now_node] + 1
                    q.append((next_node))








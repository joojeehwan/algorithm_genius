from collections import deque

MIN_VALUE = 0
MAX_VALUE = 100000

n, k = map(int, input().split())
visited = [0] * (MAX_VALUE + 1)
queue = deque([n])
visited[n] = 1

if n == k:
    print(0)
else:
    while not visited[k]:
        now_pos = queue.popleft()

        for x in [-1, 1, now_pos]:
            new_pos = now_pos + x

            if MIN_VALUE <= new_pos <= MAX_VALUE and \
                    not visited[new_pos]:
                visited[new_pos] = visited[now_pos] + 1
                queue.append(new_pos)

    print(visited[k]-1)

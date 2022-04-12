import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
queue = deque()
# A보다 작은 수는 필요 없고, B보다 큰 수는 필요 없다.
diff = B - A + 1
visited = [0] * diff
visited[0] = 1
queue.append(A)
result = -1


while queue:
    now = queue.popleft()

    for new_number in [now * 2, now * 10 + 1]:
        if new_number < B:
            visited[new_number - A] = visited[now - A] + 1
            queue.append(new_number)
        elif new_number == B:
            result = visited[now - A] + 1



print(result)
# 정답 참고
from collections import deque

MIN_VALUE = 0
MAX_VALUE = 100000

n, k = map(int, input().split())
visited = [0] * (MAX_VALUE + 1)
cnt = [0] * (MAX_VALUE + 1)
visited[n], cnt[n] = 1, 1

queue = deque([n])

while queue:
    now_pos = queue.popleft()

    for x in [-1, 1, now_pos]:
        new_pos = now_pos + x

        if MIN_VALUE <= new_pos <= MAX_VALUE:
            if not visited[new_pos]:
                visited[new_pos] = visited[now_pos] + 1
                cnt[new_pos] = cnt[now_pos]
                queue.append(new_pos)
            else:
                # 이미 여기 오긴 했는데, 이번에도 최단거리인 경우
                if visited[new_pos] == visited[now_pos] + 1:
                    cnt[new_pos] += cnt[now_pos]

print(visited[k]-1)
print(cnt[k])

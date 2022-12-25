from collections import deque

MIN_VALUE = 0
MAX_VALUE = 100000

n, k = map(int, input().split())
visited = [0] * (MAX_VALUE + 1)
routes = [0] * (MAX_VALUE + 1)

visited[n] = 1
queue = deque([n])


def search():
    path = [k]
    prev = k

    for _ in range(visited[k]-1):
        path.append(routes[prev])
        prev = routes[prev]

    print(*path[::-1])


def bfs():
    while not visited[k]:
        now_pos = queue.popleft()

        for x in [-1, 1, now_pos]:
            new_pos = now_pos + x

            if MIN_VALUE <= new_pos <= MAX_VALUE and \
                    not visited[new_pos]:
                visited[new_pos] = visited[now_pos] + 1
                routes[new_pos] = now_pos
                queue.append(new_pos)
    print(visited[k]-1)
    search()


bfs()



"""
이전풀이
"""
from collections import deque

MIN_VALUE = 0
MAX_VALUE = 100000

n, k = map(int, input().split())
visited = [0] * (MAX_VALUE + 1)
visited[n] = 1

queue = deque([n])


def find_short_time():
    while not visited[k]:
        now_pos = queue.popleft()

        for x in [-1, 1, now_pos]:
            new_pos = now_pos + x

            if MIN_VALUE <= new_pos <= MAX_VALUE and \
                    not visited[new_pos]:
                visited[new_pos] = visited[now_pos] + 1
                queue.append(new_pos)
    return visited[k]-1


def find_short_route():
    next_pos = k
    routes = [k]

    while next_pos != n:
        previous_time = visited[next_pos] - 1
        if next_pos % 2 == MIN_VALUE and visited[next_pos // 2] == previous_time:
            next_pos //= 2
        elif next_pos - 1 >= MIN_VALUE and visited[next_pos - 1] == previous_time:
            next_pos -= 1
        elif next_pos + 1 <= MAX_VALUE and visited[next_pos + 1] == previous_time:
            next_pos += 1
        routes.append(next_pos)

    return " ".join(map(str, reversed(routes)))


print(find_short_time())
print(find_short_route())

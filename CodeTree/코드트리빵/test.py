



data = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]

data.sort(key=lambda x : (x[1], x[0]))

print(data)

from collections import deque


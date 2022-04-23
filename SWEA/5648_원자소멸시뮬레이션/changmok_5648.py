# 3:35 (개거지같은거) (심지어 답지풀이)

from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


for t in range(1, int(input())+1):
    n = int(input())
    atoms = deque([])
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        x = 2 * x + 2000
        y = 2 * y + 2000
        atoms.append((x, y, d, k))
    energy = 0

    while atoms:
        field = dict()
        l = len(atoms)
        for _ in range(l):
            x, y, d, k = atoms.popleft()
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < 4001 and 0 <= ny < 4001):
                continue
            atoms.append((nx, ny, d, k))
            if (nx, ny) in field:
                field[(nx, ny)].append((d, k))
            else:
                field[(nx, ny)] = [(d, k)]

        for cx, cy in field:
            if len(field[(cx, cy)]) > 1:
                for d, k in field[(cx, cy)]:
                    atoms.remove((cx, cy, d, k))
                    energy += k

    print(f'#{t} {energy}')

# giulgi = [
#     [0, 1, 2, 4],
#     [1, 0, 4, 2],
#     [2, 4, 0, 3],
#     [4, 2, 3, 0]
# ]
#
#
# def collide(x0, y0, d0, x1, y1, d1, distance):
#     return x0 + dx[d0] * distance == x1 + dx[d1] * distance and y0 + dy[d0] * distance == y1 + dy[d1] * distance
#
#
# def check_possibilities(atms):
#     shortest_distance = 9876543210
#     dissipation = set()
#     combinations = list(itertools.combinations(atms, 2))
#     for combination in combinations:
#         x0, y0, d0, k0 = combination[0]
#         x1, y1, d1, k1 = combination[1]
#         g = giulgi[d0][d1]
#         if g == 1:
#             if x0 == x1:
#                 distance = abs((y1 - y0)//2)
#             else:
#                 distance = 9876543211
#         elif g == 2:
#             if x1 != x0 and (y1 - y0) / (x1 - x0) == 1.0:
#                 distance = abs(y1 - y0)
#             else:
#                 distance = 9876543211
#         elif g == 3:
#             if y0 == y1:
#                 distance = abs((x1 - x0)//2)
#             else:
#                 distance = 9876543211
#         elif g == 4:
#             if x1 != x0 and (y1 - y0) / (x1 - x0) == -1.0:
#                 distance = abs(x1 - x0)
#             else:
#                 distance = 9876543211
#         else:
#             distance = 9876543211
#         if distance < shortest_distance:
#             if collide(x0, y0, d0, x1, y1, d1, distance):
#                 shortest_distance = distance
#                 dissipation = {(x0, y0, k0), (x1, y1, k1)}
#         elif distance == shortest_distance:
#             if collide(x0, y0, d0, x1, y1, d1, distance):
#                 dissipation.add((x0, y0, k0))
#                 dissipation.add((x1, y1, k1))
#     return shortest_distance, dissipation
#
#
# for t in range(1, int(input())+1):
#     n = int(input())
#     atoms = []
#     for _ in range(n):
#         x, y, d, k = map(int, input().split())
#         atoms.append((2*x, 2*y, d, k))
#     energy = 0
#     while True:
#         shortest, dissipating_atoms = check_possibilities(atoms)
#         if shortest == 9876543210:
#             break
#         atoms_left = []
#         while dissipating_atoms:
#             x, y, d, k = atoms.pop()
#             if (x, y, k) in dissipating_atoms:
#                 energy += k
#                 dissipating_atoms.remove((x, y, k))
#                 continue
#             atoms_left.append((x+dx[d]*shortest, y+dy[d]*shortest, d, k))
#         atoms += atoms_left
#     print(f'#{t} {energy}')
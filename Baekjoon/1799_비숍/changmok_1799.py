def move(row, col):
    col += 1
    if col >= s:
        col = 0
        row += 1
    return row, col


def dfs(vi, bishops):
    global maximum

    if vi >= lv:
        if maximum < len(bishops):
            maximum = len(bishops)
        return

    r, c = vac[vi]

    if drd[s-1+r-c][r] and dru[r+c][c]:
        for ind in range(len(drd[s-1+r-c])):
            drd[s-1+r-c][ind] = False
        for ind in range(len(dru[r+c])):
            dru[r+c][ind] = False
        dfs(vi+1, bishops+[(r, c)])
        for ind in range(len(drd[s-1+r-c])):
            drd[s-1+r-c][ind] = True
        for ind in range(len(dru[r+c])):
            dru[r+c][ind] = True
    
    dfs(vi+1, bishops)

'''
0, 4
0, 3  1, 4
0, 2  1, 3  2, 4
'''
s = int(input())
board = [list(map(int, input().split())) for _ in range(s)]
maximum = 0

rot = []
drd = []
dru = []
vac = []

for i in range(s):
    rot.append([0] * (i+1))
    drd.append([True] * (i+1))
    dru.append([True] * (i+1))

for i in range(1, s):
    rot.append([0] * (s-i))
    drd.append([True] * (s-i))
    dru.append([True] * (s-i))

for r in range(s):
    for c in range(s):
        if board[r][c] == 1:
            rot[r+c][r-c]

lv = len(vac)

dfs(0, [])

print(maximum)


'''

'''
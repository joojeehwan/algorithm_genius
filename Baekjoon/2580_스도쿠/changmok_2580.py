def dfs(r, c):
    if r == 9:
        for row in sudoku:
            print(' '.join(list(map(str, row))))
        return True
    if sudoku[r][c]:
        if c == 8:
            return dfs(r + 1, 0)
        else:
            return dfs(r, c + 1)

    for i in range(1, 10):
        if rownums[r][i] and colnums[c][i] and tbtnums[tbt(r, c)][i]:
            rownums[r][i] = colnums[c][i] = tbtnums[tbt(r, c)][i] = False
            sudoku[r][c] = i
            if c == 8:
                if dfs(r + 1, 0):
                    return True
            else:
                if dfs(r, c + 1):
                    return True
            rownums[r][i] = colnums[c][i] = tbtnums[tbt(r, c)][i] = True
            sudoku[r][c] = 0
    return False

def tbt(r, c):
    return (r // 3) * 3 + (c // 3)


sudoku = [list(map(int, input().split())) for _ in range(9)]
rownums = [[True] * 10 for _ in range(9)]
colnums = [[True] * 10 for _ in range(9)]
tbtnums = [[True] * 10 for _ in range(9)]
for r in range(9):
    for c in range(9):
        if sudoku[r][c]:
            rownums[r][sudoku[r][c]] = False
            colnums[c][sudoku[r][c]] = False
            tbtnums[tbt(r, c)][sudoku[r][c]] = False
dfs(0, 0)
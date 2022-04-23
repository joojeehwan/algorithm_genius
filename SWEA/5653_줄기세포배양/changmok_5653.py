# 1시간 18분 (디버깅하다 졸았음)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    grid_taken = dict()
    cells_by_vitality = dict()
    vitality_prior = set()
    for row in range(n):
        for col in range(m):
            if grid[row][col]:
                vitality_prior.add(grid[row][col])
                cells_by_vitality[grid[row][col]] = cells_by_vitality.get(grid[row][col], []) + [(row, col, grid[row][col], grid[row][col], grid[row][col])]
                if row in grid_taken:
                    grid_taken[row][col] = True
                else:
                    grid_taken[row] = {col: True}
    vitality_prior = sorted(list(vitality_prior), reverse=True)
    prlen = len(vitality_prior)

    while k > 0:
        for i in range(prlen):
            vitality = vitality_prior[i]
            next_cells_by_vitality = []
            while cells_by_vitality[vitality]:
                row, col, vit, after_spread, ogvit = cells_by_vitality[vitality].pop()
                if vit > 0:
                    next_cells_by_vitality.append((row, col, vit - 1, after_spread, ogvit))
                    continue
                if vit == 0:
                    if after_spread - 1:
                        next_cells_by_vitality.append((row, col, vit - 1, after_spread - 1, ogvit))
                    for d in range(4):
                        nrow = row + dr[d]
                        ncol = col + dc[d]
                        if nrow in grid_taken:
                            if ncol in grid_taken[nrow]:
                                continue
                            else:
                                grid_taken[nrow][ncol] = True
                        else:
                            grid_taken[nrow] = {ncol: True}
                        next_cells_by_vitality.append((nrow, ncol, ogvit, ogvit, ogvit))
                    continue
                if vit < 0:
                    if after_spread - 1:
                        next_cells_by_vitality.append((row, col, vit, after_spread-1, ogvit))
            cells_by_vitality[vitality] = next_cells_by_vitality
        k -= 1

    cell_counts = 0
    for vitality in cells_by_vitality.values():
        cell_counts += len(vitality)

    print(f'#{t} {cell_counts}')
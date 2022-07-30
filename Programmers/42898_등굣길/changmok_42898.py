def solution(m, n, puddles):
    ground = [[0] * n for _ in range(m)]
    for (pr, pc) in puddles:
        ground[pr-1][pc-1] = -1
    ground[0][0] = 1
    for r in range(0, m):
        for c in range(0, n):
            if ground[r][c] != -1:
                if r > 0 and ground[r-1][c] != -1:
                    ground[r][c] = ground[r][c] + ground[r-1][c]
                if c > 0 and ground[r][c-1] != -1:
                    ground[r][c] = ground[r][c] + ground[r][c-1]
                if ground[r][c] >= 1000000007:
                    ground[r][c] %= 1000000007
        
    
    answer = ground[m-1][n-1]
    return answer
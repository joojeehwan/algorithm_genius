n, m, k ,t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
spray = [[0]*n for _ in range(n)]


D1 = ((-1,0), (1,0), (0,-1), (0,1))
D2 = ((-1,-1), (1,-1), (-1,1), (1,1))

answer = 0

def is_range(r, c):
    if r < 0 or r > n-1 or c < 0 or c > n-1:
        return False
    return True

def grow(): # 1.
    for r in range(n):
        for c in range(n):
            if board[r][c] > 0:
                curr_r, curr_c = r, c
                for i in range(4):
                    next_r = curr_r + D1[i][0]
                    next_c = curr_c + D1[i][1]

                    if not is_range(next_r, next_c):
                        continue
                    if board[next_r][next_c] > 0:
                        board[curr_r][curr_c] += 1


def spread():
    temp_board = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if board[r][c] > 0:
                curr_r, curr_c = r, c
                empty_cnt = 0
                empty_list = []
                for i in range(4):
                    next_r = curr_r + D1[i][0]
                    next_c = curr_c + D1[i][1]

                    if not is_range(next_r, next_c):
                        continue
                    if board[next_r][next_c] == 0 and spray[next_r][next_c] == 0:
                        empty_cnt += 1
                        empty_list.append((next_r, next_c))
                if empty_cnt:
                    add_value = board[curr_r][curr_c] // empty_cnt
                    for er, ec in empty_list:
                        temp_board[er][ec] += add_value

    for r in range(n):
        for c in range(n):
            board[r][c] += temp_board[r][c]
            if spray[r][c] < 0:
                spray[r][c] += 1

def kill_cnt_search(curr_r, curr_c):
    total_kill = board[curr_r][curr_c]
    for i in range(4):
        temp_k = k
        temp_r, temp_c = curr_r, curr_c
        while temp_k:
            next_r = temp_r + D2[i][0]
            next_c = temp_c + D2[i][1]
            if not is_range(next_r, next_c):
                break
            if board[next_r][next_c] == -1 or board[next_r][next_c] == 0:
                break
            total_kill += board[next_r][next_c]
            temp_r, temp_c = next_r, next_c
            temp_k -= 1
    return total_kill

def kill(): # 3.
    global answer
    result = (0,0,0)
    for r in range(n):
        for c in range(n):
            if board[r][c] > 0:
                total_kill = kill_cnt_search(r, c)

                if result < (total_kill, -r, -c):
                    result = (total_kill, -r, -c)

    
    start_r, start_c = -result[1], -result[2]
    if board[start_r][start_c] > 0:
        answer += board[start_r][start_c]
    board[start_r][start_c] = 0
    spray[start_r][start_c] = -t
    for i in range(4):
        temp_k = k
        temp_r, temp_c = start_r, start_c
        while temp_k:
            next_r = temp_r + D2[i][0]
            next_c = temp_c + D2[i][1]

            if not is_range(next_r, next_c):
                break
            if board[next_r][next_c] == -1:
                break
            if board[next_r][next_c] == 0:
                spray[next_r][next_c] = -t
                break
            answer += board[next_r][next_c]
            board[next_r][next_c] = 0
            spray[next_r][next_c] = -t
            temp_r, temp_c = next_r, next_c
            temp_k -= 1

for y in range(m):

    grow()
    spread()
    kill()

print(answer)

'''
n, m, k, t = map(int, input().split())
tree_grid = list(list(map(int, input().split())) for _ in range(n))

diag = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def in_grid(r, c):
    if r < 0 or  r > n-1 or c < 0 or c > n-1:
        return False
    return True


def check_growth(r, c):
    result = 0
    if r > 0 and tree_grid[r-1][c] > 0:
        result += 1
    if r < n-1 and tree_grid[r+1][c] > 0:
        result += 1
    if c > 0 and tree_grid[r][c-1] > 0:
        result += 1
    if c < n-1 and tree_grid[r][c+1] > 0:
        result += 1
    return result

def spread(r, c):
    result = 0
    top = bot = lef = rig = False
    if r > 0 and tree_grid[r-1][c] == 0:
        result += 1
        top = True
    if r < n-1 and tree_grid[r+1][c] == 0:
        result += 1
        bot = True
    if c > 0 and tree_grid[r][c-1] == 0:
        result += 1
        lef = True
    if c < n-1 and tree_grid[r][c+1] == 0:
        result += 1
        rig = True
    if top:
        new_tree_grid[r-1][c] += tree_grid[r][c] // result
    if bot:
        new_tree_grid[r+1][c] += tree_grid[r][c] // result
    if lef:
        new_tree_grid[r][c-1] += tree_grid[r][c] // result
    if rig:
        new_tree_grid[r][c+1] += tree_grid[r][c] // result
    

trees = 0
for y in range(m):
    # grow & spread
    new_tree_grid = list([0] * n for _ in range(n))
    for r in range(n):
        for c in range(n):
            if tree_grid[r][c] > 0:
                growth = check_growth(r, c)
                tree_grid[r][c] += growth
                spread(r, c)
    for r in range(n):
        for c in range(n):
            tree_grid[r][c] += new_tree_grid[r][c]
    
    # kill point search
    most_kill = 0
    mr = mc = -1
    for r in range(n):
        for c in range(n):
            kill_count = tree_grid[r][c]
            for d in range(4):
                dr, dc = diag[d]
                for l in range(k):
                    nr = r + dr * l
                    nc = c + dc * l
                    if not in_grid(nr, nc):
                        break
                    if tree_grid[nr][nc] == -1 or tree_grid[nr][nc] == 0:
                        break
                    kill_count += tree_grid[nr][nc]
            if kill_count > most_kill:
                most_kill = kill_count
                mr, mc = r, c
    
    for r in range(n):
        for c in range(n):
            if tree_grid[r][c] < -1:
                tree_grid[r][c] += 2

    if tree_grid[r][c] > 0:
        trees += tree_grid[r][c]
        tree_grid[r][c] = -2 * t
    elif tree_grid[r][c] < -1:
        tree_grid[r][c] -= 2 * t
    
    for d in range(4):
        dr, dc = diag[d]
        for l in range(k):
            nr = r + dr * l
            nc = c + dc * l
            if not in_grid(nr, nc):
                break
            if tree_grid[nr][nc] == -1 or tree_grid[nr][nc] == 0:
                break
            if tree_grid[nr][nc] < -1:
                tree_grid[r][c] -= 2 * t
            if tree_grid[nr][nc] > 0:
                trees += tree_grid[nr][nc]
                tree_grid[nr][nc] = -2 * t

print(trees)
'''
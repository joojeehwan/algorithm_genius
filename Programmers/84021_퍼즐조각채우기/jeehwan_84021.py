from collections import deque
import copy

global answer
answer = 0

# https://art-coding3.tistory.com/52
# 델타 배열 for bfs/dfs
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
empty_gameboard = []  # gameboard의 빈 영역(이제 곧 채워질 녀석)
block_table = []  # 테이블의 블록 값


def bfs(x, y, N, visited, array, check):
    space = []
    q = deque()
    q.append([x, y])
    space.append([x, y])
    visited[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]

            # 범위 체크
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue

            # 갈 수 있는 곳 check // 한번도 안간 곳 + 게임보드(빈곳) / 테이블(블록이 있는 곳)
            if not visited[next_x][next_y] and array[next_x][next_y] == check:
                visited[next_x][next_y] = True
                q.append([next_x, next_y])
                space.append([next_x, next_y])
    return sorted(space)


# 0, 0 기준으로 변환 => 최소 x값과 최서 y값을 0, 0으로 변환하고, 다른것들도 이동한 만큼 변환 해주어야 한다.
def standard(b, n):
    change = []
    minx = n
    miny = n
    for point in b:
        minx = min(minx, point[0])
        miny = min(miny, point[1])
    # 같은 것을 다르게 한번 해보기!
    for x, y in b:
        change.append([x - minx, y - miny])
    return sorted(change)


def rotate(b, n):
    new_board = []
    for block in b:
        new_board.append([block[1], n - 1 - block[0]])
    return sorted(standard(new_board, n))


def solution(game_board, table):
    global answer
    N = len(game_board)
    visited_gameboard = [[False for _ in range(N)] for _ in range(N)]
    visited_table = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 빈칸 0 , 이미 채워진 칸 1
            # 빈칸에다가 테이블에 있는것 넣어야 하는 것
            # 빈칸이고 아직 한번도 가지 않은 곳일때
            if game_board[i][j] == 0 and visited_gameboard[i][j] == False:
                pass  # 여기서 bfs 관련 함수가 들어가야 함.
                empty_gameboard.append(bfs(i, j, N, visited_gameboard, game_board, 0))

            if table[i][j] == 1 and visited_table[i][j] == False:
                block_table.append(bfs(i, j, N, visited_table, table, 1))

            else:
                continue

    # 찾은 table 블록 좌표를 0, 0기준으로 변환한다! 비교를 위해서!
    table_block = []
    for block in block_table:
        table_block.append(standard(block, N))

    # 찾은 gamge_board의 빈영역 좌표를 0, 0 기준으로 변환
    game_block = []
    for block in empty_gameboard:
        game_block.append(standard(block, N))

    # 이제 넣을 수 있나 비교 연산

    for g_block in game_block:
        # 그냥 바로 넣을 수 있는 경우
        if g_block in table_block:
            answer += len(g_block)
            # 한개의 배열의 값을 "값"을 찾아서 없앤다.
            table_block.remove(g_block)
        else:
            # 회전해서 넣어야 하는 경우
            flag = False
            for t_block in table_block:
                temp = copy.copy(t_block)
                # 여기서 이렇게 복사해서 사용하지 않으면!
                # for문을 돌면서, table_block의 값을 remove로 변화시키는데
                # 회전을 할때 이전의 초기의 table_block가 필요하기 때문이다

                # 4방향 한번 회전해 본다..!
                for _ in range(4):
                    if g_block == temp:
                        answer += len(g_block)
                        table_block.remove(t_block)
                        flag = True
                        break

                    temp = rotate(temp, N)
                if flag:
                    break

    return answer


#dfs 풀이로 다시 봐보자
'''

def dfs(table, i, j, shape, find = 1):
        # 우 좌 하 상
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0] 
    stack = [[i, j]] # 현재 위치 스택에 저장
    shape.append((i, j))
    
    while stack:
        a, b = stack.pop()
        table[a][b] = -1 # 방문 처리
        for i in range(4): # 우 좌 하 상 순으로 스택에 저장 -> 상 하 좌 우 순으로 꺼내져 수행된다.
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < len(table) and 0 <= y < len(table[0]) and table[x][y] == find:
                table[x][y] = -1
                stack.append([x, y])
                shape.append((x, y))
                
# 블록이나 빈 칸을 (0, 0)을 시작점으로 옮김
def rearrange(shape):
    minX = min([x[1] for x in shape])
    minY = min([x[0] for x in shape])
    shape = [(s[0]-minY, s[1]-minX) for s in shape]
    return sorted(shape) # 블록이 여러 칸으로 이루어진 경우 같은 모양에서 같은 결과를 위해 정렬해서 반환

# 여러 방향으로 회전 후 하나의 값 반환
def rotate(shape):
    if len(shape) == 1: return shape
    shapes = []
    shape = list(shape)
    shape.sort()
    width = max([x[1] for x in shape]) - min([x[1] for x in shape])
    height = max([x[0] for x in shape]) - min([x[0] for x in shape])
    # 시계 방향으로 4회 회전
    for _ in range(4):
        tmp = []
        # 시계 방향으로 회전하는 방법
        # 1. (x, y) 값을 (y, x)로 x, y를 맞바꾸는 '전치'
        for pos in shape:
            tmp.append((pos[1], pos[0])) # 전치
        # 2. 전치된 결과에서 x 좌표를 가로 길이에서 뺀다.
        tmp = [(x[0], width - x[1]) for x in tmp]
        tmp = rearrange(tmp) # 재정렬
        shape = tmp # 시계 방향으로 회전 한 블록을 shape에 다시 저장
        shapes.append(shape)
        width, height = height, width # 2x3 크기의 블록이 회전하면 3x2가 되므로 width, height를 맞바꾼다.
    
    # 4번 회전한 결과가 담긴 shapes의 최소값을 반환하면 
    # 같은 구성의 순서가 다른 리스트에서도 항상 동일한 결과 반환
    return min(shapes) 
                
def solution(game_board, table):
    # table에서 추출된 블록들과 game_board에서 추출된 빈 칸들을 저장하는 리스트
    shapes, spaces = list(), list() 
    # game_board와 table의 크기가 같다고 주어졌기 때문에 한 번에 돌릴 수 있음
    for i in range(len(table[0])):
        for j in range(len(table)):
            # table에서 블록 추출하는 dfs
            if table[i][j] == 1: # 1이면 블록
                shape = list()
                dfs(table, i, j, shape) # table에서 블록(1) 추출
                shape = rearrange(shape) # 추출한 블록 (0, 0) 부터 시작하도록 위치 값 조정
                shape = rotate(shape) # 회전 후 항상 동일한 결과 반환
                shapes.append(shape) # shapes 에서 블록들 관리
            # game_board에서 빈 칸 추출하는 dfs
            if game_board[i][j] == 0: # 0이면 빈 칸
                space = list()
                dfs(game_board, i, j, space, find = 0) # game_board에서 빈 칸(0) 추출
                space = rearrange(space) # 추출한 공백 (0, 0) 부터 시작하도록 위치 값 조정
                space = rotate(space) # 회전 후 항상 동일한 결과 반환
                spaces.append(space) # spaces 에서 공백들 관리
                
    answer = 0
    for space in spaces:
        for shape in shapes:
            if space == shape: # 같은 모양이 있다면
                answer += len(shape) # 블록의 개수만큼 더한다
                shapes.remove(shape) # 사용된 블록은 제거
                break
    return answer

'''
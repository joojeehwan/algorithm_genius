'''

만들어야 하는 함수


1) 에어컨 바람 나오기


2) 시원한 공기들 섞이기 


3) 외벽에 있는 칸 1씩 감소

'''


from collections import deque

#왼쪽 위 오른쪽 아래
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]


def air_con(row, col, dir):

    # 에어컨 바로 앞에 벽이 있을 경우
    if wall[row][col][dir]:
        return

    # 이 값을 반환 해서, 복사해도 되고, 그냥 반환 떄려도 되고
    air = [[0] * n for _ in range(n)]

    #처음 시작 한 칸은 일단 5값이 생긴다. 그 다음 칸부터, 4, 3, 2, 1 이렇게 떨어짐.
    next_row = row + dr[dir]
    next_col = col + dc[dir]
    air[next_row][next_col] = 5
    q = deque()
    q.append((next_row, next_col, 5))

    while q:

        next_row, next_col, cold = q.popleft()

        # 차가운 공기가 없는 경우
        if not cold:
            break

        # 3가지 방향이 존재 한다. 
        '''
        오른쪽 방향 기준
        
        위 대각선
        오른쪽 정면
        아래 대각선
        '''
        paths = [[(dir-1+4) % 4, dir], [(dir+1) % 4, dir], [dir] ]

        for path in paths:

            now_cold_row = row
            now_cold_col = col
            flag = True
            for k in path :
                next_cold_row = now_cold_row + dr[k]
                next_cold_col = now_cold_col + dc[k]

                # 벽이 있거나, 범위를 벗어난 경우
                if not (0 <= next_cold_row < n and 0 <= next_cold_col < n) or wall[row][col][k]:
                    flag = False
                    break
            #공간에 갈 수 있고, 차가운 공기가 들어있지 않은 경우 (안 가본 곳)
            if flag and not air[next_cold_row][next_col]:
                air[next_row][next_col] = cold - 1
                q.append((next_cold_row, next_cold_col, cold - 1))

    return air


# 찬 공기 섞기

def air_mix():

    # temp 배열을 통해서, 값을 "동시"에 변화 시키고
    # result 배열에 값을 전부 넣자.
    
    '''
    
    여기서 더 확실해지는 temp를 쓰는 이유

    지금

    8 4 1     6 6 1
    2 9 3  => 4 7 3
    2 1 4     2 1 4

    가 되기 위해서 mix의 작업을 거쳐야 하는데,
    이를 하는데, 원본이 바뀌어 버리면 안된다. 
    즉 , 왼쪽에서 8이랑 2랑 이미 mix 하고 그 다음에 7, 3으로 그 다음 mix를 진행하는 것이 아님
    따라서 원본을 그대로 두기 위함.

    여기선 for문을 통해서 복사를 했지만,
    deepcopy를 사용해도 무방하다.

    이게 바로 진정 "동시에"의 의미.

    '''

    temp = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n) : 
            temp[row][col] = result[row][col]


    #실제 작업 부분
    for row in range(n):
        for col in range(n):
            for dir in range(4):
    
    
                #벽 있으면 안 썩힘
                if wall[row][col][dir]:
                    continue

                next_row = row + dr[dir]
                next_col = col + dc[dir]
                
                #범위를 벗아날 경우

                if not (0 <= next_row < n and 0 <= next_col < n):
                    continue
                #많은 쪽은 줄어들고, 적은 쪽은 더 생겨야 하므로!
                if result[row][col] > result[next_row][next_col]:
                    temp[row][col] -= (result[row][col] - result[next_row][next_col]) // 4

                else:
                    temp[row][col] += (result[next_row][next_col] - result[row][col]) // 4


    #이제 동시에 반영을 시키자!

    for row in range(n):
        for col in range(n):
            result[row][col] = temp[row][col]


#벽 쪽만 다 줄이자!
def air_reduce():

    x, y = n-1, n-1

    # 왼, 위, 오, 아 의 벡터 배열을 사용해서!
    # 범위 벗어나는 경우만 없앤다.
    # 격자무늬 우 하단 에서 부터 시작해서 범위 바뀌면 방향 바뀌는 스타일 활용
    
    # 그 다음 방향을 위함
    for i in range(4):
        # 범위 안나가면 쭉 그 방향 그대로 가서 다 줄여버리기
        while True:
            x, y = x+dr[i], y+dc[i]
            if not (0 <= x < n and 0 <= y < n):
                x, y = x-dr[i], y-dc[i]
                break
            if result[x][y]:
                result[x][y] -= 1


def more_than_k():
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 1 and result[i][j] < k:
                return False
    return True

#초기 입력

# 격자 크기 n, 벽의 개수 m, 원하는 사무실의 시원함 정도 k
n, m, k = map(int, input().split())

MAP = [list(map(int, input().split()))]

# 한번에 모든 배열의 값을 정리해서 담을 result 배열

result = [[0] * n for _ in range(n)]

#2차원 배열인데, 그 값이 벽이 사방향 중에 어디 있는 지를 나타내는 배열
wall = [[[False] * 4 for _ in range(n)] for _ in range(4)]


for _ in range(m):

    row, col, dir = map(int, input().split())

    if dir == 0 :
        #위
        wall[row - 1][col - 1][dir + 1] = True

        #아래
        wall[row -2][col -1 ][dir + 3] = True


    else:

        #왼쪽, dir = 1

        wall[row - 1][col - 1][dir - 1] = True

        #오른쪽

        wall[row - 1][col-2][dir + 1] = True
        


for ans in range(1, 101):

    for row in range(n):
        for col in range(n):
            if MAP[row][col] >= 2:
                # -2를 하는 이유?! 좌 상 우 하
                # 2, 3, 4, 5 를 우리가 정한 벡터 배열에 맞게 끔 하기 위함.
                # 0, 1, 2, 3 => 그래서 벡터 배열 자체도 좌 상 우 하로 설계
                air = air_con(row, col, MAP[row][col] - 2)

                #각각 air con 한거 합치기
                for i in range(n):
                    for j in range(n):
                        result[i][j] += air[i][j]

    air_mix()
    air_reduce()
    if more_than_k():
        print(ans)
        break

    else:
        if ans == 100:
            print(-1)
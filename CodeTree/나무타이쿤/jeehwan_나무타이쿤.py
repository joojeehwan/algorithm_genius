'''


1)  특수 영양제가 이동규칙에 따라 이동하고, 땅에 특수 영양제 투입

2) 영양제 투입한 리브로수의 대각선으로 인접(4방향)한 높이가 1 이상인 리브로수의 크기

만큼 높이가 더 성장. (MAP을 벗어나는 건 세지 않는다.)

3) 초기 영양제가 있는 곳과 이동 후에 영양제가 있는 곳을 제외하고, 높이 2만큼을 잘라내고, 다시 그곳에 특수 영양제를 뿌린다.




'''


#기본입력 및 세팅

n,m = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(n)]

#8방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

#diagonal 대각선 4방향
dia_dr = [-1, -1, 1, 1]
dia_dc = [-1, 1, -1, 1]

#굳이 하나의 MAP으로 만 할 필요가 없다! 메모리를 더 사용하더라도, 이렇게 이차원 배열로 표시
fertilizer = [[False] * n for _ in range(n)]
fertilizer_area = []
# 초기 영양제 있는 곳

for row in range(n - 2, n):
    for col in range(2):
        fertilizer[row][col] = True

def stop_one(dir, p):

    global fertilizer, fertilizer_area
    temp = [[False] * n for _ in range(n)]
    #만약에 위에 fertilizer_area 없이 하면, 아래는 이 함수 안에서의 새로운
    # 배열로 생성..! 위에 GLOBAL로 가져오는 게 중요! 가만 보면 아래도 할당이구먼!
    fertilizer_area = []
    for row in range(n):
        for col in range(n):
            #fertilizer 이 2차원 배열에 기록을 했기 떄문에 이렇게 편하게 사용이 가능
            if fertilizer[row][col] :
                next_row = (row + dr[dir - 1] * p) % n
                next_col = (col + dc[dir - 1] * p) % n
                temp[next_row][next_col] = True
                fertilizer_area.append((next_row, next_col))

    fertilizer = temp[:]


def stop_two():
    global fertilizer

    #일단 영양제 있는 곳이 1씩 증가 하고 시작
    for row, col in fertilizer_area:
        MAP[row][col] += 1
        
    #대각선 체크해서 더 성장
    for row, col in fertilizer_area:
        for k in range(4):
            next_row = row + dia_dr[k]
            next_col = col + dia_dc[k]

            #범위 체크
            if 0 <= next_row < n and 0 <= next_col < n and MAP[next_row][next_col] >= 1:
                MAP[row][col] += 1

    #동시에 모든 영양제 재투여를 한꺼번에 하기 위함.
    temp = [[False] * n for _ in range(n)]

    #특수 영양제 재 공습
    for row in range(n):
        for col in range(n):
            # 높이가 2이상이면서 , 영양제가 없었던 곳! 이것 때문이라도 영양제의 위치
            #를 기록하기 위한 이차원 배열이 필요 함.
            if MAP[row][col] >= 2 and not fertilizer[row][col]:
                MAP[row][col] -= 2
                temp[row][col] = True

    fertilizer = temp[:]


#시물레이션 시작
for _ in range(m):
    d, p = map(int, input().split())

    stop_one(d,p)

    stop_two()
    debug = 1
ans = 0

for row in range(n):
    for col in range(n):
        ans += MAP[row][col]

print(ans)

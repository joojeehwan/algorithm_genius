'''


크게 구현 해야 하는 것.

1. 토네이도의 이동 (회전)

    항상 시작은
    start_row = N // 2
    start_col = N // 2

    좌 -> 하 -> 우 -> 상

    매 순간 방향을 바꾸면 쉽게 구현?!(단, visited[][] 배열로 check 하면서 가야함)

2. 이동에 따른 모래의 이동

 - 방향에 따른 모래의 이동 비율 설정하기
 => ( 배열을회전..?! / 미리 델타 배열같이 만들어 두거나)

미리, 토네이도 이동 4방향에 따른 y 위치를 기준으로 y의 모래가 이동하는 table을 구현


결국 구해야 하는 건, 격자박으로 나간 모래의 양을 구해야 한다.

참고)

https://www.youtube.com/channel/UC_KRcBNnFQoN6EsvG87H6cg
https://unie2.tistory.com/992
'''



n = int(input())

MAP = [list(map(int, input().split())) for _ in range(n)]

start_row, start_col = n // 2, n // 2

#델타배열의 이동 좌 하 우 상 // 그냥 막 하면 안돼!

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

#이동에 따른 모래의 이동 => 미리 토네이도의 이동 방향
sand_row = [
    #토네이도 이동 방향의 기준에 따른
    #좌
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    #하
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    #우
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    #상
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]

sand_col = [
    # 토네이도 이동 방향의 기준에 따른
    # 좌
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # 하
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # 우
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # 상
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]
#실제 비율
rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

#위에 3개를 하나의 테이블로 생각 같이 움직인다.

def movingSand(row, col, dir):
    answer = 0 #격자 밖의 모래양
    sand = MAP[row][col]
    total_ratio_sands = 0 #비율의 모래들이 모이는! sand에서 빼면 알파의 값이 되겟지

    #1. 비율 모래 이동
    #9가지 비율의 모래 날림.
    for i in range(9):
        next_row = row + sand_row[dir][i]
        next_col = col + sand_col[dir][i]
        ratio_sand = (sand * rate[i]) // 100
        total_ratio_sands += ratio_sand

        #격자 밖! value 값 더해줘야 한다.
        if not (0 <= next_row < n and 0 <= next_col < n):
            answer += ratio_sand
            continue
        # 격자 밖인 경우엔, 아래 로직을 탈 필요 없다.
        # 기존에 있던 모래에 더해진다. => 격자 밖의 모래를 모하러?!
        MAP[next_row][next_col] += ratio_sand

    #2. 비율 이외의 모래 이동
    #비율 외 알파로 가는 모래 이동 => 정정당당히 좌 하 우 상의 이동
    next_row = row + dr[dir]
    next_col = col + dc[dir]
    a = sand - total_ratio_sands
    #격자 밖
    #알파 마저도, 격자 밖으로 이동할 수 있다.
    if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n :
        answer += a
    else:
        # 기존에 있던 모래에 더해진다.
        MAP[next_row][next_col] += a
    #기존에 자리에 있던 모래가, 알파와 비율의 모래로 전부 다 이동했으니, 0으로 바꿔준다.
    MAP[row][col] = 0
    return answer

def solve(row, col):

    answer = 0
    visited = [[False] * n for _ in range(n)]
    dir = -1 #아무 방향 x, 방향은 0 ~ 4에 적용 되어 있음.
    while True :
        #(0,0)에 도착 => 토네이도의 이동을 멈춘다.
        if row == 0 and col == 0:
            break
        visited[row][col] = True
        next_dir = (dir + 1) % 4
        next_row = row + dr[next_dir]
        next_col = col + dc[next_dir]

        if visited[next_row][next_col] :
            #가려는 곳을 이미, 방문했기에 나선형을 만족하기 위해서, 다음 방향이 아닌, 이곳에 왓을때의 방향으로 다시
            next_dir = dir
            next_row = row + dr[next_dir]
            next_col = col + dc[next_dir]

        answer += movingSand(next_row, next_col, next_dir)
        #여기서 dir이 바뀌게 되고...
        row, col, dir = next_row, next_col, next_dir

    return answer


result = solve(start_row, start_col)

print(result)












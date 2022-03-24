



# 바둑판 입력받기

MAP = [list(map(int, input().split())) for _ in range(19)]

loc = 0

# 우상, 우, 우하, 하 4가지 방향 check
dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for row in range(19):
    for col in range(19):

        if MAP[row][col] == 0:
            continue

        #방향 설정
        for k in range(4):
            cnt = 0
            #해당 방향으로 얼마만큼 이동할 것인가 => 오목체크
            for i in range(5):
                next_row = row + dr[k] * i
                next_col = col + dc[k] * i
    
                #범위 확인
                if 0 <= next_row < 19 and 0 <= next_col < 19 :
                    # cnt증가 시키기
                    if MAP[next_row][next_col] == MAP[row][col]:
                        cnt += 1

            #육목체크 알고리즘 => 시작의 반댓 방향과 마지막의 다음방향으로 같은 돌이 1개라도 있으면 육목이 되어버린다.
            next_row = row - dr[k]
            next_col = col - dc[k]

            if  0 <= next_row < 19 and 0 <= next_col < 19 and MAP[row][col] == MAP[next_row][next_col]:
                continue

            #그 이후 방향으로 하나라도 더 있으면 안됌.
            next_row = row + dr[k] * 5
            next_col = col + dc[k] * 5

            if 0 <= next_row < 19 and 0 <= next_col < 19 and MAP[row][col] == MAP[next_row][next_col]:
                continue

            #육목 체크 후에도 돌이 5개라면, 즉 5목이라면
            if cnt == 5:
                answer_row = row
                answer_col = col
                loc = MAP[row][col]
print(loc)
if loc != 0:
    print(answer_row + 1, answer_col + 1)



'''

https://ywtechit.tistory.com/150님의 풀이

n = 19
arr = [list(map(int, input().split())) for _ in range(n)]
 
dx = [1, 1, 0, -1]    # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]    
 
def omok():
    for x in range(n):
        for y in range(n):
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1
 
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
 
                    while 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny]:
                        cnt += 1
 
                        if cnt == 5:
                            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:    # 육목 판정 1
                                break
                            if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and arr[x][y] == arr[x - dx[i]][y - dy[i]]:    # 육목 판정 2
                                break
                            return arr[x][y], x+1, y+1    # 육목이 아닌 오목이면 return
 
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1    # 승부가 나지 않을 때
 
color, x, y = omok()
if not color:
    print(color)
else:
    print(color)
    print(x, y)

'''
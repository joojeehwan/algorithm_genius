'''

어른 상어

상어는 다른 상어의 냄새가 없는 공간으로 이동함.
동시에 같은 공간에 존재하면 번호가 낮은 상어만 살아남음.
k시간 만큼 상어의 냄새는 남아있음.
이동할 곳이 없으면 자신의 냄새가 있던 곳으로 돌아감.


시물레이션 + bfs 문제


priorities : 미리 정해진 방향정보를 저장할 리스트
smell : 현재 시간에 냄새의 상황을 보여주는 리스트
data : 상어의 현재 위치를 나타내는 리스트

저 3개의 data 구조가 어떻게 이루어지는 파악하는게 중요,,!
index처리 주의
'''


n, m, k  = map(int, input().split())

#처음 상어 위치
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))


#상어의 초기 방향 정해
directions = list(map(int, input().split()))

#상어의 방향별 우선순위 받아오기(위 아래 왼쪽 오른쪽)
#리스트 컴프리핸션 말고도 이런식으로 입력 받을 줄도 알아야 해
prioritites = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))

    prioritites.append(temp)



#델타 배열 -> 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#상황판 그리기(상어 번호, 냄새가 머무는 시간)

smell = [[[0, 0]] * n for _ in range(n)]


#모든 냄새 정보 업데이트

def update_smell():
    for i in range(n):
        for j in range(n):
            #냄새가 남아 있는 경우 => 시간이 지나서 -1 만큼 감소 시켜야 함
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            #상어가 존재하는 위치의 경우 => 냄새를 뿌린다. k로 설정하기!
            if data[i][j] != 0:
                smell[i][j] = [data[i][j], k]


# 모든 상어를 이동시키는 함수

def move():
    #이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_data = [[0] * n for _ in range(n)]
    #각 위치를 순회
    for row in range(n):
        for col in range(n):
            #상어가 존재
            if data[row][col] != 0:
                dir = directions[data[row][col] - 1] #현재 상어의 방향,, 왜 1을 빼지?! => 상어의 번호는 1번 부터 시작! but 초기 방향의 index는 0번부터 시작이니! -1을 한것!
                found = False
                #일단 냄새가 존재하지 않는 곳인지 확인하기
                for index in range(4):
                    # prioritites엔 여러 상의 정보가 담김, 그중에서 data[row][col] - 1는 상어 번호는 1 부터 시작이지만 index는 아니라서!
                    # 상어에 맞는 우선순위를 찾고, 그 다음에 dir-1 은 dir은 방향을 나타냄 1~4 그러나 이것도 index로 들어가서 찾아야 하니 -1을 한것
                    # 마지막 index는 그러한 우선순위가 4개씩 있는데(가로로) 그것을 탐색하게 하는 키워드 인것! 여기서도 -1을 하는 이유는
                    # dr, dc 델타배열에서 index값에 맞게 맞는 방향을 찾기 위함!
                    next_row = row + dr[prioritites[data[row][col] - 1][dir-1][index] - 1]
                    next_col = col + dc[prioritites[data[row][col] - 1][dir-1][index] - 1]
                    #일단 장외인지 확인
                    if 0 <= next_row < n and 0 <= next_col < n:
                        if smell[next_row][next_col][1] == 0 : #냄새가 나지 않는 곳이라면
                            #해당 상어의 방향 이동시키기
                            directions[data[row][col] -1 ] = prioritites[data[row][col] - 1][dir - 1][index]
                            # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
                            # 상어 이동시키기

                            if new_data[next_row][next_col] == 0:
                                new_data[next_row][next_col] = data[row][col]
                            else:
                                new_data[next_row][next_col] = min(data[row][col], new_data[next_row][next_col])
                            found = True
                            break
                if found:
                    continue
                #주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동

                for index in range(4):
                    next_row = row + dr[prioritites[data[row][col] - 1][dir - 1][index] - 1]
                    next_col = col + dc[prioritites[data[row][col] - 1][dir - 1][index] - 1]
                    if 0 <= next_row < n and 0 <= next_col < n:
                        if smell[next_row][next_col][0] == data[row][col]: #자신의 냄새가 있는 경우라면
                            #해당 상어의 방향 이동 시키기
                            directions[data[row][col] - 1] = prioritites[data[row][col] - 1][dir - 1][index]
                            #상어 이동시키기
                            new_data[next_row][next_col] = data[row][col]
                            break
    return new_data


answer = 0
while True:
    update_smell() #모든 위치의 냄새를 업데이트
    new_data = move() #모든 상어를 이동시키기
    data = new_data #맵 업데이트
    answer += 1 #시간 증가

    #1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            #1 이상이라는건 1번 상어 이외의 상어가 존재 한다는 것! 그래서 False
            if data[i][j] > 1:
                check = False

    if check:
        print(answer)
        break
    if answer >= 1000:
        print(-1)
        break
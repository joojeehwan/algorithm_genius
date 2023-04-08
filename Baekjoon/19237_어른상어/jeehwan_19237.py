'''

어른 상어

1.
N*N 격자에 M개의 칸에 상어가 한마리씩 들어 있고, 자신의 위치에 냄새를 뿌림 
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고
자신의 냄새를 그 칸에 뿌림
k시간 만큼 상어의 냄새는 남아있음

2.
상어는 다른 상어의 냄새가 없는 공간으로 이동함.
이동할 곳이 없으면 자신의 냄새가 있던 곳으로 돌아감.
이 때, 이동할 수 있는 칸이 여러개 있을 수 있는데 => 특정 우선순위를 따른다.

3.
동시에 같은 공간에 존재하면 번호가 낮은 상어만 살아남음. (즉 1번 번호의 상어만이 결국엔 격자에 살아 남음)


1번 상어가 격자에 남게 되긲지 걸리는 시간을 출력하라


시물레이션 + bfs 문제


1 : 위
2 : 아래
3 : 왼쪽
4 : 오른쪽

priorities : 미리 정해진 방향정보를 저장할 삼차원 리스트 , priorities[상어번호][이동방향][방향 별 우선순위] = 이동방향
=> 해당 방향으로 진행하지 못할 경우 , "방항 별 우선순위"의 인덱스 값을 변화시켜, 상어의 다음 이동방향을 구한다.  


smell : 현재 시간에 냄새의 상황을 보여주는 이차원 리스트 , smell [row][col] = [상어번호, 남은 냄새 시간]
                                                 => smell[row][col][0] = 해당 row, col의 상어번호
                                                 => smell[row][col][1] = 해당 row, col의 남은 냄새 시간
                                                 
data : 상어의 현재 위치를 나타내는 이차원 리스트(MAP), data[row][col] = row, col에 위치하고 있는 상어 번호

directions : 상어의 현재 방향

저 3개의 data 구조가 어떻게 이루어지는 파악하는게 중요,,!

index처리 주의
'''


n, m, k  = map(int, input().split())

#처음 상어 위치(MAP)
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
    for _ in range(4) :
        temp.append(list(map(int, input().split())))

    prioritites.append(temp)
'''
[
   [
    위쪽일 때 우선순위   []  
    아래일 때 우선순위   []
    왼쪽일 때 우선순위   []
    오른일 때 우선순위   []               
                        ]  =>이런게 상어마다 있는 것!
    
                          ]

'''
print(prioritites)
#델타 배열 -> 상 하 좌 우, 문제에 주어진 대로 적음
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#상황판 그리기(상어 번호, 냄새가 머무는 시간)

smell = [[[0, 0]] * n for _ in range(n)]
#smell2 = [[0, 0] * n for _ in range(n)]
print(smell)
#print(smell2)

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
                    # prioritites 자료구조 분석
                    # data[row][col] - 1 :  상어 번호. 데이터는 1 부터 시작이지만, prioritites는 0부터 시작하는 index 라서 -1을 함.
                    # dir-1 : 현재 상어의 이동방향.  해당 상어의 방향도 1부터 시작 하지만, prioritites 0부터 시작하는 index 라서 -1을 함.
                    # index : 현재 방향 별 이동 우선순위.
                    # prioritites[data[row][col] - 1][dir-1][index] - 1 에서 마지막에 -1을 하는 이유!? "상어번호별"의 "현재 방향"에 따른 "이동 우선순위" 도 1부터 시작하기에! 인덱스를 맞추기 위함.
                    next_row = row + dr[prioritites[data[row][col] - 1][dir-1][index] - 1]
                    next_col = col + dc[prioritites[data[row][col] - 1][dir-1][index] - 1]
                    #일단 장외인지 확인
                    if 0 <= next_row < n and 0 <= next_col < n:
                        if smell[next_row][next_col][1] == 0 : #냄새가 나지 않는 곳이라면
                            # 해당 상어의 방향을 이동을 했으니, "상어번호별"의 "현재 방향"에 따른 "이동 우선순위" 에 따른 방향으로 바꾼다!
                            # directions은 항상 상어의 현재 방향을 기억하는 배열임.

                            directions[data[row][col] -1] = prioritites[data[row][col] - 1][dir - 1][index]

                            # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
                            # 상어 이동시키기

                            #상어가 아무도 없는 경우는 그냥 들어간다. 
                            if new_data[next_row][next_col] == 0:
                                new_data[next_row][next_col] = data[row][col]
                                
                            # 상어가 존재하는 경우는 더 낮은 번호의 상어가 들어갈 수 있도록 함
                            # 여기서 주의 min의 비교는 data[row][col]와 new_data[next_row][next_col]를 하는 것!
                            # new_data[row][col] 와 new_data[next_row][next_col]를 하는 것이 아님.
                            else:
                                new_data[next_row][next_col] = min(data[row][col], new_data[next_row][next_col])
                            found = True
                            # 격자를 탐색하면서, 그 다음
                            break
                            
                # 해당 found 변수를 통해, 4방향 탐색 이후에도 모두 냄새가 있는 경우를 체크해 
                # 모두 냄새가 있는 경우엔 continue를 타지 못해, continue 아래의 부분 로직이 실행되도록
                if found:
                    continue

                #4방향 모두 들러봤는데도, 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
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
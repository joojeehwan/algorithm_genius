
'''

백준  어른 상어와 같은 문제

승자독식 모노폴리 


-- 이동 우선순위


독점계약이 없는 칸 > 자신의 독점계약이 있는 칸(이떄 가능한 칸이 여러개, 플러이어마다 마다 다른 우선순위)


    우선순위 : 플레이어마다 다름 + 같은 플레이어라 해도, 현재 바라보고 있는 방향에 따라서도 달라진다. 


-- 독점계약은 k 시간 만큼 유지 됨


-- 동시에 같은 칸에, 2개 이상의 플레이어가 있을 시에, 번호가 낮은 플레이어만 살아남는다. 



1 상 
2 하
3 좌
4 우 


-- 초기 자료구조 생각

3개 모두 격자에 row, col으로 표시 
# priorities : 미리 정해진 방향 정보를 저장
# contract : 현재 시간에 독점계약 상황을 보여주는 리스트 
# data : 현재 플레이어의 위치를 나타내는 리스트 


1차원 리스트
# directions : 상어의 초기 방향을 저장

'''

# 정리 -- python의 배열 복사 관련
# n = 4
# test = [[False] * n for _ in range(n)]

# test[0][1] = True
# print(test)


# test1 = [[[0, 0] for _ in range(4)] for _ in range(4)]
# test1[0][0][0] = 1
# test1[0][0][1] = 2
# print(test1)

# n = 3
# temp_data = [[0] * n for _ in range(n)]

# temp_data[0][1] = 100

# print(temp_data)


# 이전 내 풀이 복습하기.

n, m, k = map(int, input().split())

# 초기 플레이어 위치

data = [list(map(int, input())) for _ in range(n)]
'''
혹은

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))
'''

# 상어의 초기 방향 설정

directions = list(map(int, input().split()))

# 상어별

'''
굳이 리스트 컴프리해션을 사용하지 않고, 이렇게 하는 이유?!

4개씩 끊어서 담기 위함. 

상어마다, 초기바라보는 방향 별로, 우선순위가 달라지는 데

이를 위해 4개씩 끊어서 생각

'''
priorities = []

for _ in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))

    # 위에 for문에서, 각 플레어이 별 우선순위를 다 넣고, 한번에 append 하기에
    # priorities[상어 번호][상어가 바라보는 방향][상어의 우선 순위(여기에 있는 값으로 실제 이동이 진행 됨)]
    priorities.append(temp)

# 2차원 배열 인데, 값 안의 값이 리스트 인것

'''

[   
   플렝이어 1 [ [,,]          ] 
    [               ]
    [               ]    
    [               ] 
                        ]

이런 형태로 데이터 
'''

# 델타 배열 설정 => 문제에 주어진 숫자 번호 대로 상 하 좌 우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# contract 상황판 만들기
# 각각의 2차원 배열마다, 거기에 누가 들어가 있는지?! 냄새가 얼마나 지속되는지
# 이거 이렇게 하면 다 같이 바뀌는 데 그래도 답이 맞네..!? 뭘까...?!
# contract = [[[0, 0]] * n for _ in range(n)]

# 아래와 같이 적어야, 각 row, col 마다 []의 값을 넣어서 값을 다르게 반영

# 격자의 각각 row, col 별 [플레이어 번호, 독점계약 유지 기간]

contract = [[[0, 0] for _ in range(n)] for _ in range(n)]


# 모든 독점 계약 정보 update

def update_contract():
    for row in range(n):
        for col in range(n):

            # 독점 계약이 남아있는 경우, 시간의 흐름에 따라 값이 -1
            if contract[row][col][1] > 0:
                contract[row][col][1] -= 1

            # 플레이어가 존재하는 위치에, 독점계약 맺기 => k 시간 만큼 지속되니깐
            if data[row][col] != 0:
                contract[row][col] = [data[row][col], k]


# 모든 플레이어 이동 시키는 함수


def move():
    # 이동의 결과를 저장하기 위한 임시 자료구조
    temp_data = [[0] * n for _ in range(n)]

    '''
    굳이 이렇게, 이동의 결과를 저장하기 위한 임시 자료구조를 만드는 이유?!

    기존의 원본 data를 건드려, 다음의 반복에서 원본 데이터가 아닌 수정된 값으로 로직을 수행하지 않도록 하기 위함.

    '''

    # 각 위치를 순회

    for row in range(n):
        for col in range(n):

            if data[row][col] != 0:

                dir = directions[data[row][col] - 1]

                # 주변에 모두 독점계약이 있으면, 다시 자신의 냄새가 있는 곳으로 가야하니
                # 독점계약 할 곳을 찾는다면, True // 아니라면 False
                # 이를 위한 flag 변수를 두자
                found = False

                for index in range(4):

                    # 이동해보자

                    next_row = row + dr[priorities[data[row][col] - 1][dir - 1][index] - 1]
                    next_col = col + dc[priorities[data[row][col] - 1][dir - 1][index] - 1]

                    # 이동 후에 장외 판단

                    if 0 <= next_row < n and 0 <= next_col < n:

                        # 독점계약이 없는 곳이라면 바로 이동
                        if contract[next_row][next_col] == 0:

                            # 플레이어의 초기 방향 update, 이동 후에는 이동한 쪽의 방향을 바라보게 된다.
                            directions[data[row][col] - 1] = priorities[data[row][col] - 1][dir - 1][index]

                            # 더 낮은 번호의 플레이어가 우선순위

                            if temp_data[next_row][next_col] == 0:

                                # 현재 반복을 돌리고 있는 row, col을 내가 찾은 next_row, next_col으로 격자내에서 이동
                                temp_data[next_row][next_col] = data[row][col]

                            else:

                                # 새롭게 추가되는 플레이어의 번호랑(data[row][col]) 기존에 해당 격자에 있떤 플레이어 번호(temp_data[next_row][next_col])
                                temp_data[next_row][next_col] = min(data[row][col], temp_data[next_row][next_col])

                            found = True
                            break

                # 독점계약을 이미 한 곳은 내 독점계약이 있던 곳으로 다시 안돌아가도 된다.
                # 따러서
                if found:
                    continue

                # 다시 자신의 독점계약이 있는 곳으로 돌아가기
                for index in range(4):

                    next_row = row + dr[priorities[data[row][col] - 1][dir - 1][index] - 1]
                    next_col = col + dc[priorities[data[row][col] - 1][dir - 1][index] - 1]

                    if 0 <= next_row < n and 0 <= next_col < n:

                        # 내 독점계약이 있는 곳을 찾기
                        if contract[next_row][next_col][0] == data[row][col]:
                            # 내 독점계약이 있는 곳으로 가면서, 바뀐 내 방향을 update
                            directions[data[row][col] - 1] = priorities[data[row][col] - 1][dir - 1][index]

                            # 다시 내 독점계약이 있는 곳으로 가자
                            temp_data[next_row][next_col] = data[row][col]
                            break

    return temp_data


answer = 0

while True:

    update_contract()
    new_data = move()
    data = new_data  # update 된 값으로 MAP 갱신
    answer += 1  # 시간을 1씩 증가
    check = True

    for row in range(n):
        for col in range(n):

            # 아 아직 1번 이상인 번호가 있네?!
            if data[row][col] > 1:
                check = False

    if check:
        print(answer)
        break
    if answer >= 1000:
        print(-1)
        break








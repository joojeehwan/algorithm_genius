'''


1) 경주 시작 준비

- P마리의 토끼가, N, M 격자 위에서 시물레이션

- i번 토끼의 고유 번호 -> pidi / 이동해야 하는 거리 -> di

- 1, 1 행에서 출발 => (0, 0)을 (1,1)로 본다.


2) 경주 진행

- 우선순위가 높은 토끼 선정 후 이동 k번 진행

    *) 토끼 결정
        1. 현재까지의 총 점프 횟수가 적은 토끼
        2. 현재 서 있는 행 번호 + 열 번호가 작은 토끼
        3. 행 번호가 작은 토끼
        4. 고유번호가 작은 토끼


    *) 결정 후 이동

        우선순위에 의해 토끼 선정 이후, 4방향으로 di 만큼 이동, 4방향중 아래의 우선순위를 통해 방향 결정
        격자를 벗어나게 되면 방향을 반대로 바꿔 한 칸 이동 => "하나의 지구라 생각" 모둘려 연산

        1. 행 번호 + 열 번호가 큰 칸
        2. 행 번호가 큰 칸
        3. 열 번호가 큰 칸

        이동 후의 좌표를 (ri, ci)라고 했을 때, 현재 이동한 토끼를 제외한 나머지 p - 1 마리의 토끼들이 전부 (ri + ci)만큼 점수를 얻음

        k번동안 진행되는 동안 동일한 토끼가 여러번 선택 될 수 있음.


- k번 턴이 모두 진행된 이후에는 아래의 우선순위를 통해, 점수 S를 더 주게 됨. 단 이경우는 앞선 k번의 반복에서 "선택"된 토끼 중에서 선택해야 함.

     1. 현재 서 있는 행 번호 + 열번호가 큰 토끼
     2. 행 번호가 큰 토끼
     3. 열 번호가 큰 토끼




3) 이동거리 변경

고유번호가 pidt인 토끼의 이동거리를 L배 (단, 토끼의 이동거리는 10억을 넘어가지 않는다.)


4) 최고의 토끼 선정

각 토끼가 모든 경주를 진행ㅇ하며 얻은 점수 중 가장 높은 점수를 출력

Q번에 걸쳐 명령을 순서대로 진행하며, 최고의 토끼를 선정해주는 프로그램을 작성해라


'''




Q = int(input())

# 1) 경주 시작 준비
def readyForRace(object) :

    N, M, P = object[0], object[1], object[2]

    rabbitNumber_distance = {}

    for i in range(P):
        rabbitNumber_distance[object[3 + (i*2)]] = object[3 + (i*2) + 1]




# 2) 경주 주행

def race(object):
    pass

# 3) 이동거리 변경

def changeDistance(object):
    pass


# 4) 최고의 토끼 선정
def selectBestRabbit() : 
    pass

for _ in range(Q):

    temp = map(int, input().split())

    if temp[0] == 100:
        readyForRace(temp[1:])

    elif temp[0] == 200:
        race(temp[1:])

    elif temp[0] == 300:
        changeDistance(temp[1:])

    else:
        selectBestRabbit()

from collections import deque

n, k = map(int, input().split())
#deque를 이렇게도 쓸 수가 있구만,,!
belt = deque(map(int, input().split()))
robots = deque([0] * 2 * n)
level = 1

while True:
    #1. 벨트가 한칸 회전
    belt.rotate(1)
    robots.rotate(1)
    #그림속에선 1부터 시작이라,,!로봇이 내려가는 곳이라 robots[n-1]은 0 이 되는것이 맞다.
    robots[n-1] = 0
    #2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동한다.
    #만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i + 1] and belt[i + 1]:
            belt[i + 1] -= 1 #벨트의 내구도 떨어뜨리고
            robots[i + 1], robots[i] = robots[i], 0 #i + 1로 로봇이 이동하고, 원래 있던 자리엔 로봇이 없으니 0으로
    #위에서 조건을 만족한다면, 로봇의 이동이 있었을텐데, 따라서 "떨어지는 위치"에선 로봇이 없어야 하므로
    robots[n-1] = 0

    #3. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아있어야한다.
    #올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if not robots[0] and belt[0]:
        robots[0] = 1
        belt[0] -= 1
    #4.내구도가 0인 칸의 개수가 k개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if belt.count(0) >= k:
        print(level)
        break

    level += 1
    

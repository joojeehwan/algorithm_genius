from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * N)

"""
1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
"""

cnt = 0
while 1:
    cnt += 1
    # 1. 벨트, 로봇 회전
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    # 2. 로봇 이동
    if sum(robot):      # 로봇이 존재한다면
        for i in range(N-1):
            if robot[N-i-1] and not robot[N-i] and belt[N-i]:
                robot[N-i] = robot[N-i-1]
                robot[N-i-1] = 0
                belt[N-i] -= 1
        robot[-1] = 0
    # 3. 로봇 올리기
    if belt[0] and not robot[0]:
        robot[0] = 1
        belt[0] -= 1
    # 4. 내구도 검사
    if belt.count(0) >= K:
        break

print(cnt)
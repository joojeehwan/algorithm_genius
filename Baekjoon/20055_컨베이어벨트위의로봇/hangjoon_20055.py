from collections import deque
import sys


length, limit = map(int, sys.stdin.readline().split())  # 컨베이어 벨트 길이, 내구도 0인 칸의 개수 한계
durable_lst = deque(map(int, sys.stdin.readline().split()))  # 컨베이어 벨트 내구도 리스트

start = 0  # 올리는 위치
end = length - 1  # 내리는 위치
robots = deque([0]) * (length * 2)

cnt = 0
while durable_lst.count(0) < limit:
    cnt += 1  # 단계 + 1

    # 1. 벨트 한 칸씩 이동
    durable_lst.appendleft(durable_lst.pop())
    robots.appendleft(robots.pop())

    # 2. 로봇 한 칸씩 이동
    for robot_idx in range(length - 1, 0, -1):
        if robot_idx == end and robots[robot_idx]:  # 로봇이 내리는 위치에 도착
            robots[robot_idx] = 0  # 로봇 내리기
        if robots[robot_idx] and not robots[robot_idx + 1] and durable_lst[robot_idx + 1]:  # 로봇이 있고 다음 칸에 로봇이 없고 내구도가 있으면
            robots[robot_idx] -= 1  # 이동 시작
            robots[robot_idx + 1] += 1  # 이동 끝
            durable_lst[robot_idx + 1] -= 1  # 내구도 감소
        if robot_idx + 1 == end and robots[robot_idx + 1]:  # 로봇이 내리는 위치에 도착
            robots[robot_idx + 1] = 0  # 로봇 내리기

    # 3. 올리는 위치에 로봇 올리기
    if durable_lst[start]:
        robots[start] = 1  # 로봇 올리기
        durable_lst[start] -= 1  # 내구도 감소

print(cnt)
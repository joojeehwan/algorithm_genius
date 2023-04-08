import sys


house, router = map(int, sys.stdin.readline().split())  # 집 수, 공유기 수
house_lst = [0] * house  # 집 좌표 리스트
for i in range(house):
    house_lst[i] = int(sys.stdin.readline())
house_lst.sort()
ans = 0

"""
거리를 기준으로 잡아서 이분 탐색을 실시한다.
최대 거리가 x라고 가정했을 때, 필요한 router의 개수가 문제에서 주어진 것과 같아질 때 정답!
"""

start = 1  # 가장 가까운 간격
end = house_lst[-1] - house_lst[0]  # 가장 먼 간격
while start <= end:
    center = (start + end) // 2  # 공유기 간격
    now = house_lst[0]  # 현재 위치
    cnt = 1  # 공유기 개수
    for i in range(house):
        if house_lst[i] - now < center:  # 공유기 범위 안
            continue
        else:  # 공유기 범위 밖
            now = house_lst[i]  # 새로운 범위
            cnt += 1  # 공유기 수 추가

    if cnt < router:  # 너무 띄엄띄엄 = 거리 간격을 줄여야함
        end = center - 1
    else:  # 너무 촘촘 = 거리 간격을 늘려야함
        start = center + 1
        ans = center


print(ans)


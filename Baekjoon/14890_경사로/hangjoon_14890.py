def is_road(lst, size, slide):
    road = 0
    cnt = 1  # 연속 평지 수
    for i in range(size - 1):
        if abs(lst[i] - lst[i + 1]) >= 2:  # 높이 차이가 큼
            return 0
        elif lst[i] == lst[i + 1]:  # 같은 높이
            cnt += 1
        else:  # 높이 차이가 1
            if lst[i] < lst[i + 1]:  # 올라가기
                if cnt >= slide:  # 경사로 설치 가능
                    cnt = 1
                    continue
                else:  # 불가능
                    return 0
            else:  # 내려가기
                if i + slide >= size:  # 맵 밖
                    return 0
                if sum(lst[i + 1: i + 1 + slide]) // slide == lst[i + 1]:  # 설치 가능
                    cnt = -slide + 1 # 이미 설치
                    continue
                else:  # 공간 부족
                    return 0

    else:
        road += 1
    return road


size, slide = map(int, input().split())  # 맵 크기, 경사로 길이
field = [[] for _ in range(size)]  # 격자 상태
for r in range(size):
    field[r] = list(map(int, input().split()))
ans = 0

# 왼쪽에서 오른쪽으로
for start_row in range(size):
    ans += is_road(field[start_row], size, slide)

# 위에서 아래로
for start_col in range(size):
    temp = []
    for now_row in range(size):
        temp.append(field[now_row][start_col])
    ans += is_road(temp, size, slide)

print(ans)
row, col = map(int, input().split())  # 열, 행 크기
box = [[] for _ in range(row)]  # 상자
for r in range(row):
    box[r] = list(map(int, list(input())))

ans = 1
for r in range(row - 1):  # 시작 열
    for c in range(col - 1):  # 시작 행
        for cc in range(c + 1, col):  # 탐색 행
            length = cc - c  # 정사각형 한 변의 인덱스 차이(= 길이 - 1)
            # 가지치기
            if r + length >= row:  # 박스 밖임
                continue
            if (length + 1) ** 2 <= ans:  # 기존 박스가 더 큼
                continue
            # 판별
            if box[r][c] == box[r][cc]:  # 같은 열에 동일 숫자 찾음
                key = box[r][c]  # 꼭지점 수
                if box[r + length][c] == key and box[r + length][cc] == key: # 같은 행, 같은 길이에 동일 숫자 찾음
                    ans = (cc - c + 1) ** 2
print(ans)
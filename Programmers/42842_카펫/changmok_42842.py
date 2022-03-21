def solution(brown, yellow):
    answer = []
    ra = 0
    ca = 0

    # 가로보다 길지 않은 세로 노란색 값에 대하여
    for yc in range(1, int(yellow ** (1/2)) + 1):

        # 정수로 떨어지는 가로, 세로의 값이 아니라면 제외
        if yellow % yc != 0:
            continue

        # 세로 값에 맞춘 가로값 저장
        yr = yellow // yc

        # 노란색을 감싸는 테두리 한 줄의 칸 수 계산 결과가 갈색과 일치한다면 결과 저장
        if (yc + 2) * (yr + 2) - yellow == brown:
            ra = yr + 2
            ca = yc + 2

        # 정답을 찾고난 후의 추가적인 연산은 불필요함
        if ra and ca:
            break

    answer = [ra, ca]

    return answer
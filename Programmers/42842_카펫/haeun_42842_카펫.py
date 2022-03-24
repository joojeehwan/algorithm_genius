def solution(brown, yellow):

    sum_tile = brown + yellow
    search = (sum_tile) // 2

    for height in range(2, search + 1):
        width = sum_tile // height
        # 약수가 아니라면 (나눴는데 0으로 안 떨어지면) 볼 필요가 없다.
        if sum_tile % width:
            continue

        brown_test = 2 * (width + height - 2)
        yellow_test = (width - 2) * (height - 2)

        if brown_test == brown and yellow_test == yellow:
            return [width, height]

print(solution(24, 24))
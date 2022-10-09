# 중력 함수
def gravity():
    # 중력 작용을 쉽게 구현하기 위해
    # temp 배열을 활용합니다.
    for i in range(n + 1):
        for j in range(1, MAX_WIDTH + 1):
            temp[i][j] = 0

    for j in range(1, MAX_WIDTH + 1):
        # 아래에서 위로 올라오면서
        # 해당 위치에 블록이 있는 경우에만 temp에
        # 쌓아주는 식으로 코드를 작성할 수 있습니다.
        # 진짜 겁나 쉬운 방법인듯...
        last_idx = n
        for i in range(n, -1, -1):
            if bucket[i][j]:
                temp[last_idx][j] = bucket[i][j]
                last_idx -= 1

    # 다시 temp 배열을 옮겨줍니다.
    for i in range(n + 1):
        for j in range(1, MAX_WIDTH + 1):
            bucket[i][j] = temp[i][j]


# 범위 확인 함수
def in_range(x, y):
    return 0 <= x and x <= n and 1 <= y and y <= MAX_WIDTH



# 재귀는 이렇게
def find_max_score(cnt):
    # 여기서 cnt는 떨어지는 블럭 중 위치가 정해지지 않은 블럭의 개수
    global max_score

    # 떨어질 위치들을 전부 결정하게 되면, 직접 시뮬레이션을 통해
    # 점수를 계산하고, 그 중 가장 큰 점수를 갱신합니다.
    if cnt == len(undicided_indices):
        max_score = max(max_score, score())
        return

    # 4개의 위치 중 어느 위치에 블럭을 떨어뜨릴 것인지를 결정합니다.
    for i in range(1, MAX_WIDTH + 1):
        k, _ = given_blocks[undicided_indices[cnt]]
        given_blocks[undicided_indices[cnt]] = (k, i)
        find_max_score(cnt + 1)



# 가능한 모든 조합에 대해 점수를 계산해줍니다.
find_max_score(0)
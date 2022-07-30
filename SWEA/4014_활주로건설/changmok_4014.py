# 58분 40초

def downhill(hill, i, n):
    level = hill[i]
    for ti in range(i, i + x):
        if ti >= n or line[ti] != level:
            return -1
    if i + x == n:
        return n
    elif i + x < n:
        if hill[i+x] == level:
            return i+x
        elif hill[i+x] == level - 1:
            return downhill(hill, i+x, n)
        else:
            return -1


def check(line):
    last = line[0]
    same_level = 1
    i = 1
    while i < n:
        if last == line[i]:
            same_level += 1
        elif abs(last - line[i]) >= 2:
            return False
        elif line[i] == last + 1:
            if same_level < x:
                return False
            else:
                last = line[i]
                same_level = 1
        elif line[i] == last - 1:
            i = downhill(line, i, n)
            if i == -1:
                return False
            elif i < n:
                last = line[i]
                same_level = 1
        i += 1
    return True


for t in range(1, int(input())+1):
    n, x = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    # 행별 점검
    for r in range(n):
        line = []
        for c in range(n):
            line.append(ground[r][c])
        if check(line):
            answer += 1

    # 열 점검
    for c in range(n):
        line = []
        for r in range(n):
            line.append(ground[r][c])
        if check(line):
            answer += 1

    print(f'#{t} {answer}')
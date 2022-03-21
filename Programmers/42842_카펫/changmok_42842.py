def solution(brown, yellow):
    answer = []
    ra = 0
    ca = 0
    for yc in range(1, int(yellow ** (1/2)) + 1):
        if yellow % yc != 0:
            continue
        yr = yellow // yc
        if yc > yr:
            break
        if (yc + 2) * (yr + 2) - yellow == brown:
            ra = yr + 2
            ca = yc + 2

    answer = [ra, ca]

    return answer
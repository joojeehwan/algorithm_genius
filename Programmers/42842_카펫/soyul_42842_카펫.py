def solution(brown, yellow):
    answer = []

    can = []            # 가능한 가로 세로 경우를 모두 모아줌 (yellow 의 약수의 조합들)
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            can.append((yellow // i, i))

    for i in can:                          # 그중에서 조건을 만족하는 경우를 구함
        if (i[0] + i[1]) * 2 + 4 == brown:
            answer.append(i[0] + 2)
            answer.append(i[1] + 2)
            break
    return answer

print(solution(10, 2))
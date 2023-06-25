def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    for i in range(len(score)):
        # index를 m개씩 자르기
        if (i + 1) % m == 0:
            answer += score[i] * m

    return answer


# 풀이 2
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)

    for i in range(0, len(score), m):
        tmp = score[i:i + m]

        if len(tmp) == m:
            answer += min(tmp) * m

    return answer


# 풀이 3
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    apple_box = []
    for i in range(0, len(score), m):
        apple_box.append(score[i:i+m])
    for apple in apple_box:
        if len(apple) == m:
            answer += min(apple) * m

    return answer



# 풀이 4
def solution(k, m, score):
    answer = 0

    score.sort()

    length = len(score)

    start_point = length % m

    while start_point < length:
        answer += score[start_point] * m
        start_point += m

    return answer
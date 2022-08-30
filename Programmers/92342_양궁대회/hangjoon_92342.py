def score(me, you):
    me_score, you_score = 0, 0
    for i in range(11):
        if you[i] and me[i] <= you[i]:
            you_score += 10 - i
        elif me[i] > you[i]:
            me_score += 10 - i
    return me_score - you_score


def dfs(lion, info, n, cnt=0, start=0):
    global answer, temp
    # 종료조건
    if cnt >= n:
        res = score(lion, info)  # 점수 계산
        # 지금이 더 점수 차이가 크거나 같음
        if temp <= res:
            return res
        # 기존이 더 점수 차이가 큼
        return 0
    # 진행 중 (완탐)
    for i in range(start, 11):
        if lion[i] > info[i]:  # 이미 이긴 라운드는 패스
            continue
        lion[i] += 1
        result = dfs(lion, info, n, cnt + 1, i)
        if result:  # 라이언이 이김
            if result > temp:  # 기존 점수보다 더 큰 점수 차이
                temp = result
                answer = lion[:]
            elif result == temp:  # 동점임
                for j in range(10, -1, -1):
                    if lion[j] > answer[j]:  # 이번 경우가 더 낮은 점수를 많이 맞춤
                        answer = lion[:]
                        break
                    elif lion[j] < answer[j]:  # 기존 경우가 더 낮은 점수를 많이 맞춤
                        break
        lion[i] -= 1


def solution(n, info):
    global answer, temp
    answer = []
    temp = 0
    # 완전탐색? DFS?
    lion = [0] * 11
    dfs(lion, info, n)
    if not answer:  # 라이언이 이기는 경우 없음
        answer = [-1]
    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
def solution(prices):

    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):               # for 문을 돌면서 가격이 적은 것의 개수 카운트
            cnt += 1
            if prices[j] < prices[i]:
                break
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3]))
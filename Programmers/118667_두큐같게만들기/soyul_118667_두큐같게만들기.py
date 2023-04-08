from collections import deque

def solution(queue1, queue2):

    sum1, sum2 = sum(queue1), sum(queue2)

    deque1, deque2 = deque(queue1), deque(queue2)       # 시간을 줄이기 위해 deque로 변환

    flag = len(queue1) * 3                              # 종료 조건
    answer = 0
    while sum1 != sum2:
        answer += 1
        if answer >= flag:
            return -1
        if sum1 < sum2:
            sum1 += deque2[0]
            sum2 -= deque2[0]
            deque1.append(deque2.popleft())
        else:
            sum2 += deque1[0]
            sum1 -= deque1[0]
            deque2.append(deque1.popleft())

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
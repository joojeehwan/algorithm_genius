from collections import deque

#하나의 리스트로 풀기
def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) // 2
    cur = sum(queue1)
    queue3 = queue1 + queue2 + queue1

    s = 0
    e = len(queue1) - 1
    answer = 0
    while True:
        if cur == target:
            return answer
        if cur < target:
            e += 1
            if e >= len(queue3):
                return -1
            cur += queue3[e]
        else:
            cur -= queue3[s]
            s += 1
        answer += 1
    return answer

from collections import deque

def solution(queue1, queue2):
    answer = 0
    mid = (sum(queue1) + sum(queue2)) // 2
    leftSum = sum(queue1)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while queue1 and queue2:
        if leftSum > mid:
            tmp = queue1.popleft()
            leftSum -= tmp

        elif leftSum < mid:
            tmp = queue2.popleft()
            leftSum += tmp
            queue1.append(tmp)

        else:
            return answer
        answer += 1

    return -1

from collections import deque


def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)

    for _ in range(300001):
        # 2개중에 더 큰 값을 찾아,
        # 뺸다. => 그래야 점점 같아 지겟지?!
        # 큰 값을 뺴야?!
        if sum1 > sum2:
            sum1 -= q1[0]
            sum2 += q1[0]
            # 맨앞 뺴기
            temp = q1.popleft()
            # 맨뒤 넣기
            q2.append(temp)

        elif sum1 < sum2:

            sum1 += q2[0]
            sum2 -= q2[0]
            temp = q2.popleft()
            q1.append(temp)

        else:
            return answer

        answer += 1

    return -1
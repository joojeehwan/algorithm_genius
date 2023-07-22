# defaultdict를 사용한 풀이
from collections import defaultdict

def solution(X, Y):
    s1 = defaultdict(int)
    s2 = defaultdict(int)
    answer = []
    for s in X:
        s1[s] += 1
    for s in Y:
        s2[s] += 1

    for i in range(9, -1, -1):
        for j in range(min(s1[str(i)], s2[str(i)])):
            answer.append(str(i))
    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'
    return ''.join(answer)


def solution(X, Y):
    result = ''
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in X:
        value = int(i)
        a[value] += 1

    for i in Y:
        value = int(i)
        b[value] += 1

    for i in range(9, -1, -1):
        value = str(i) * min(a[i], b[i])
        result += value

    if (len(result) == 0):
        return '-1'
    if (result[0] == '0'):
        return '0'

    return result


def solution(X, Y):
    answer = ''

    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer


from collections import Counter


def solution(X, Y):
    # 숫자 개수 세기
    nums = Counter(X) & Counter(Y)
    if not nums:
        return '-1'  # 공통 없는 경우
    elif list(nums) == ['0']:
        return '0'  # 0만 공통인 경우

    nums_order = sorted(list(nums), reverse=True)  # 내림차순 정렬
    answer = ''
    for num in nums_order:
        answer += num * nums[num]
    return answer
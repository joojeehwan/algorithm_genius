def solution(arr):
    answer = []
    while arr:
        now = arr.pop(-1)
        if not answer or answer[-1] != now:  # 새로운 패턴 등장
            answer.append(now)
        else:  # 연속임
            continue
    return answer[::-1]


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
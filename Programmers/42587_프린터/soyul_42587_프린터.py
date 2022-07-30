def check(priorities):           # 현재 맨 앞에 있는 것보다 우선순위가 높은 것이 있는지 검사하는 함수
    prior = priorities[0]
    for i in range(1, len(priorities)):
        if priorities[i] > prior:
            return 0                     # 만약 우선순위가 높은 것이 있다면 return 0
    return 1

def solution(priorities, location):

    answer = 0

    while 1:
        if location == 0:                    # 내가 프린트하고 싶은 것이 맨 앞에 오면
            if check(priorities):           # 나보다 우선순위가 높은 게 없으면 끝
                answer += 1
                break
            else:                           # 우선순위가 높은 게 있으면 맨 뒤로 보내고 location 갱신
                priorities.append(priorities[0])
                priorities.pop(0)
                location = len(priorities) - 1
        else:
            if check(priorities):               # 나보다 우선순위가 높은 게 없으면 print
                priorities.pop(0)
                answer += 1
            else:
                priorities.append(priorities[0])
                priorities.pop(0)
            location -= 1

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
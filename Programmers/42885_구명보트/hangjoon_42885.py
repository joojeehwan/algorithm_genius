from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        end = people.pop()
        answer += 1
        if people and people[0] + end <= limit:  # 탈 수 있음
            people.popleft()
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([40, 50, 150, 160], 200))
print(solution([100, 500, 500, 900, 950], 1000))
print(solution([50], 60))
print(solution([40, 40, 40], 120))


"""
def solution(people, limit):
    answer = 0
    # 가장 limit에 가깝게 매칭
    people.sort()
    while people:
        start, end = 0, len(people) - 1  # 가벼운 사람 + 무거운 사람
        while start < end:
            if people[start] + people[end] > limit:  # 너무 무거움
                end -= 1  # 더 가벼운 사람
            elif people[start] + people[end] == limit:  # 딱 맞음
                people.pop(end)
                people.pop(start)
                answer += 1
                break
            else:  # 너무 가벼움
                start += 1  # 더 무거운 사람
        else:  # 매칭 안됨
            people.pop(start)
            answer += 1
    return answer

"""
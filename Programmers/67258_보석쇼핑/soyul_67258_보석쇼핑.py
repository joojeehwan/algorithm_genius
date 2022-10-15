"""
투포인터와 딕셔너리를 이용
"""

def solution(gems):

    set_gems = set(gems)

    right = 0
    left = 0
    min_len = len(gems)
    my_gems = {}
    answer = [1, len(gems)]

    while right < len(gems):                 # 먼저 처음부터 끝까지 검사하면서 딕셔너리에 개수를 넣어줌
        if gems[right] in my_gems:
            my_gems[gems[right]] += 1
        else:
            my_gems[gems[right]] = 1

        right += 1

        if len(my_gems) == len(set_gems):           # 훔친 보석의 개수와 보석 종류의 개수가 같으면 검사
            if my_gems[gems[left]] >= 2:            # 2개 이상이면 왼쪽 포인터를 이동
                while my_gems[gems[left]] >= 2:
                    my_gems[gems[left]] -= 1
                    left += 1
                if right - left < min_len:          # 최솟값 갱신
                    min_len = min(min_len, right - left)
                    answer = [left + 1, right]
            else:                                   # 2개 이상이 아니면 = 왼쪽 포인터를 움직일 필요가 없으면 최솟값만 갱신
                if right - left < min_len:
                    min_len = min(min_len, right - left)
                    answer = [left + 1, right]

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
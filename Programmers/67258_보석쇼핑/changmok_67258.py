from collections import defaultdict

def solution(gems):
    least = int(1e9)
    len_gems = len(gems)
    allGemsCount = len(set(gems))
    end = 0
    temp = defaultdict(int)
    for start, gem in enumerate(gems):
        while len(temp) < allGemsCount and end < len_gems:
            temp[gems[end]] += 1
            end += 1
        if len(temp) == allGemsCount:
            if least > end-start:
                least = end-start
                result = [start+1, end]
        temp[gem] -= 1
        if temp[gem] == 0:
            del(temp[gem])
    return result


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
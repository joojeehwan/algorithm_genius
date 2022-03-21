from itertools import permutations

def solution(numbers):
    length = len(numbers)

    # 순열 생성
    permutationset = set() # 중복을 포함하지 않기 위해 set()로 선언
    for l in range(1, length + 1):
        strnums = permutations(numbers, l)
        for strnum in strnums:
            num = int(''.join(strnum))
            permutationset.add(num)

    # 에라토스테네스의 체
    permutationset -= set([0, 1])
    for i in range(2, int(max(permutationset) ** 0.5) + 1):
        permutationset -= set(range(i * 2, max(permutationset) + 1, i))

    answer = len(permutationset)
    
    return answer

print(solution("011"))
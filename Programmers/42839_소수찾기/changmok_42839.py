from itertools import permutations

def solution(numbers):
    # 순열의 최대 크기를 구하기 위한 입력받은 문자열의 길이
    length = len(numbers)

    # 순열 생성
    permutationset = set() # 중복을 포함하지 않기 위해 set()로 선언

    # 1 부터 최대 크기까지 각 크기에 맞춰 순열 생성
    for l in range(1, length + 1):
        strnums = permutations(numbers, l) # 각 순열은 튜플의 형태로 모든 튜플은 permutation 객체로 저장되어 있음
        for strnum in strnums: # 각 튜플마다
            num = int(''.join(strnum)) # 단일 문자열로 join -> int()로 정수로 형변환
            permutationset.add(num) # 해당 순열의 수를 순열 집합에 추가

    # 에라토스테네스의 체
    permutationset -= set([0, 1]) # 0과 1은 소수가 아니다
    for i in range(2, int(max(permutationset) ** 0.5) + 1): # 2 부터 집합 최대값까지 에라토스테네스의 체 로직을 수행
        permutationset -= set(range(i * 2, max(permutationset) + 1, i)) # i의 배수 집합을 한번에 순열 집합에서 소거

    answer = len(permutationset) # 모든 소수가 아닌 수를 걸러낸 집합 크기가 정답
    
    return answer

print(solution("011"))
def solution(numbers, target):
    answer = 0

    l = len(numbers)
    s = [(0, 0)] # 스택

    # DFS
    while s:
        numscalculated, calculation = s.pop() # numscalculated : 계산에 포함된 숫자의 갯수 (계산할 숫자의 인덱스와 일치) / calculation : 계산 결과
        if numscalculated == l:         # l개 만큼 계산을 완료한 경우 탐색 종료
            if calculation == target:       # 만약 결과값이 target과 일치하면
                answer += 1                 # answer 증가
            continue

        nex = numbers[numscalculated] # 다음 계산할 숫자
        s.append((numscalculated + 1, calculation + nex)) # 덧셈
        s.append((numscalculated + 1, calculation - nex)) # 뺄셈

    return answer
from itertools import permutations
# permutations : 순서 중요, combinations : 순서 상관 X

def solution(numbers):
    answer = 0
    num_cnt = len(numbers)  # 배열의 크기
    num_sets = []  # 순열로 만든 숫자들 넣을 배열
    # 1부터 배열의 크기만큼 증가하며 순열들을 배열로 만들고 num_sets에 추가
    for i in range(1, num_cnt + 1):
        perm_nums = list(permutations(numbers, i))
        num_sets += perm_nums

    # ["1","7"] 과 같은 배열을 하나로 합치고 숫자로 변환하고 set를 활용해 중복을 제거한다.
    int_nums = set()
    for num in num_sets:
        int_nums.add(int(''.join(num)))

    # 소수인지 검증하는 단계
    for number in int_nums:
        # 0과 1은 소수가 될 수 없다.
        if number > 1:
            # 소수라고 가정하고 현재 숫자의 제곱근까지 보면서(시간 단축)
            palin = True
            for i in range(2, int(number ** (1 / 2)) + 1):
                # 예로 10을 1이 아닌 2로 나눈 나머지가 0이라는 점에서 소수가 아니게 된다.
                if number % i == 0:
                    palin = False
                    break
            # 반복문을 다 돌았는데 소수라는 가정이 바뀌지 않았으면 소수이므로 answer수 증가
            if palin:
                answer += 1

    return answer
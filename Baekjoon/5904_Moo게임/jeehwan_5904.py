'''

M 사이에 O의 갯수가 2개 3개 2개 4개 ... 계속 반복

S(n) = S(n-1) + 'm' + ('o' * (n+2)) + S(n-1)
     = 2 * S(n-1) + 'm' + ('o' * (n+2))
문자열의 길이로 보면, len_S(n) = 2 * len_S(n-1) + n + 3

문자열 중 몇 번째 자리에 어떤 것이 들어가는지만 판단하면 되기 때문에, 문자열 자체보다는 문자열의 길이 및 인덱스로 판단

'''


def make_some_moo(current_degree, len_of_prev_degree, target_idx):
    len_of_next_degree = 2 * len_of_prev_degree + (current_degree + 3)

    # 목표하는 자릿수가 3 이하라면 S(0) 안에서 해결되므로, 별도의 과정 없이 바로 결과 반환
    if target_idx <= 3:
        radish = 'moo'
        return radish[target_idx - 1]

    # 문자열의 길이가 목표값보다 작아 결과를 낼 수 없을 때, 차수를 1 올려 다시 문자열 길이 구하기
    elif len_of_next_degree < target_idx:
        return make_some_moo(current_degree + 1, len_of_next_degree, target_idx)
    # 문자열을 나눠보면, 앞부분인 len_S(n-1)과 / 중간 부분인 n+3 / 뒷부분인 len_S(n-1)으로 분할 가능

    # 문자열의 길이가 목표값보다 크거나 목표값과 같아졌을 때
    else:
        # 목표값이 문자열 앞부분에 있을 때
        # 사실 필요 없는 부분
        # 새로운 차수의 문자열을 만든다는 것은, 이전 차수의 문자열 안에 목표값이 없다는 것
        # 새 문자열의 중간 부분 이전은 이전 차수와 같으므로 어차피 해당 부분 내에는 목표값이 없다
        if len_of_prev_degree > target_idx:
            return make_some_moo(1, 3, target_idx)

        # 목표값이 문자열 중간 부분에 있을 때
        elif len_of_prev_degree < target_idx <= len_of_prev_degree + current_degree + 3:
            # 목표값 인덱스에서 이전 차수의 길이만큼이 빠진 것이 1인 것, 다르게 말하면 중간 부분의 첫 문자는 무조건 m
            if target_idx - len_of_prev_degree == 1:
                return 'm'
            # 중간 부분 중 첫 문자가 아닌 것은 모두 o
            else:
                return 'o'
        # 목표값이 문자열 뒷부분에 있으면, 앞부분과 중간 부분을 모두 잘라내고 목표값 위치를 변경해 뒷부분을 앞부분처럼 사용하며 다시 반복
        else:
            return make_some_moo(1, 3, target_idx - (len_of_prev_degree + current_degree + 3))

target = int(input())
print(make_some_moo(1, 3, target))
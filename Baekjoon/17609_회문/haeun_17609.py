T = int(input())

# 수정은 딱 한번만! 이 함수는 각 문자열마다 딱 2번 불려진다.
def check(edit_chars):
    check_half_len = len(edit_chars) // 2
    if len(edit_chars) % 2:
        # 홀수면 중앙 문자 제거하고 뒤집어서 비교
        if edit_chars[:check_half_len] != edit_chars[check_half_len+1:][::-1]:
            return False
    else:
        # 짝수면 그냥 뒤집어서 비교
        if edit_chars[:check_half_len] != edit_chars[check_half_len:][::-1]:
            return False
    return True


for _ in range(T):
    chars = list(input())
    half_len = len(chars) // 2
    last = len(chars) - 1
    pure_palindrome = True
    fixed = False

    for i in range(half_len):
        if chars[i] != chars[last - i]:
            # 일단 0은 될 수 없다.
            pure_palindrome = False
            # 서로 안맞는 문자열 중 왼쪽을 지워본다. 또는 오른쪽을 지워본다.
            if check(chars[i+1:last-i + 1]) or check(chars[i:last-i]):
                fixed = True
            # 여기서 검증 했으면 그만 봐도 되겠는데?
            break

    if pure_palindrome:
        print(0)
    elif fixed:
        print(1)
    else:
        print(2)
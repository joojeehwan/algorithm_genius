def short(num, s):

    word = ""
    i = 0
    j = i + num
    while i < len(s):
        if s[i:j] == s[j:j + num]:                          # num 개씩 잘라서 비교하는데 압축 가능하다면
            p = 1
            while s[i:j] == s[j:j + num]:
                p += 1                                      # 몇 번 반복하는지 검사해서 word에 반복횟수 + 반복 문자 붙여줌
                i += num
                j = i + num
            word += (str(p) + s[i:j])
        else:                                               # 압축 불가능하다면 그냥 그대로 붙임
            word += s[i:j]
        i += num
        j = i + num

    return len(word)

def solution(s):

    answer = len(s)
    for i in range(1, len(s) // 2 + 1):                # 문자열 단위를 줄일 것을 1부터 시작해서 모두 검사
        answer = min(answer, short(i, s))

    return answer

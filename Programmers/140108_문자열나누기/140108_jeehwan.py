def solution(s):
    answer, cnt1, cnt2 = 0, 0, 0

    currentChar = ""

    for targetChar in s:

        # 첫문자 갯수가 0이다 => 처음 시작
        # 따라서, 처음 시작 단어를 currentChar에 저장
        if cnt1 == 0:
            currentChar = targetChar

        # 반복문에서 현재 보고 있는 targetChar 단어가, currentChar와 똑같다?!
        # 똑같다면, cnt1 증가 아니라면 cnt2 증가

        if targetChar == currentChar:
            cnt1 += 1
        else:
            cnt2 += 1

        # 정답처리 부분
        if cnt1 == cnt2:
            answer += 1
            cnt1 = 0
            cnt2 = 0
    # 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없는 부분 처리
    if cnt1 > 0:
        answer += 1

    return answer
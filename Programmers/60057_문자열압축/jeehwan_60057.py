



def solution(s):

    answer = len(s)

    # 1개 단위부터 압축 단위를 늘려가며 확인한다.

    #길이의  반까지가 줄일 수 있는 최대의 범위
    for step in range(1, len(s) // 2 + 1):

        compress = ""
        #0에서 스텝만큼 문자열을 추출한다
        str_lst = s[0:step]
        count = 1

        #스텝의 단위만큼 증가 시키면서 이전 글자와 비교하기!
        for j in range(step, len(s), step):
            # 이전 상태 추출한것과와 지금 글자의 슬라이싱 한게 같다면, 횟수 증가!
            if str_lst == s[j : j + step]:
                count += 1
            #다른 문자열이 나옴! 같은 것이 없음
            else:
                #문자열 반복되는것 만큼 숫자로 뭉쳐주기!
                if count >= 2:
                    #숫자 + 추출한것
                    compress += str(count) + str_lst

                else:
                    compress += str_lst

                #다시 그 다음 탐색해야 하니깐
                str_lst = s[j:j + step]
                count = 1

        #남아 있는 문자열 처리
        if count >= 2:
            compress += str(count) + str_lst
        else:
            compress += str_lst

        answer = min(answer, len(compress))

    return answer
'''

4가지 발음밖에 하지 못함.

연속된 2가지의 발음을 하지 못함.

"candi = candi.replace(pro, ' ')" 에서,

" ' ' " 이어야 하는 이유
ex) yayae는 발음이 불가능한 단어임. ''로 하게 되면
aya => ye => ''로 발음이 가능한 단어로 판별

그래서, yayae를 처음에 aya 판별할 때, y e로 나오게 해, 발음을 할 수 없는 문자열로 인식하도록 함.


'''


def solution(babbling):
    pronounce = ["aya", "ye", "woo", "ma"]
    answer = 0
    for candi in babbling:
        for pro in pronounce:
            if pro * 2 not in candi:
                # 연속으로 나오지 않으면, 공백으로 대체
                candi = candi.replace(pro, ' ')

        # if candi.strip() == '':
        #     answer += 1
        if candi.isspace():
            answer += 1

    return answer
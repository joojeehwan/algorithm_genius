
'''

문자열 s

s의 각 위치마다 자신보다 앞에 나왔으면서, 
자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지..! 


'''

def solution(s):

    answer = []
    word_dict = {}

    for index, word in enumerate(list(s)):

        if word not in word_dict:
            answer.append(-1)
            #가장 최신의 글자 기록
            #word_dict[word] = index
        else:
            answer.append(index - word_dict[word])
            #가장 최신 글자 기록 최신화
            #word_dict[word] = index
        word_dict[word] = index
    return answer
from itertools import product

def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']

    dictionary = []

    # 모든 문자의 조합을 만들어주고 정렬 후 index를 찾는다
    for i in range(1, 6):
        vowel_list = list(product(vowel, repeat = i))
        for vowel_word in vowel_list:
            dictionary.append(''.join(list(vowel_word)))

    dictionary.sort()

    answer = dictionary.index(word) + 1
    return answer

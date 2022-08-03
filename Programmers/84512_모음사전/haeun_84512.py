from itertools import product
vowels = ["A", "E", "I", "O", "U"]


def solution(word):
    dictionary = set()
    for i in range(1, 6):
        result = list(product(vowels, repeat=i))
        len_result = len(result)
        for j in range(len_result):
            result[j] = "".join(result[j])
        dictionary = dictionary.union(set(result))
    dictionary = sorted(list(dictionary))

    return dictionary.index(word)+1



print(solution("EIO"))

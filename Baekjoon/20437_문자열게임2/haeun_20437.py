"""
K개 이상 있어야 검증할 가치가 있으므로, 각 소문자의 등장 횟수를 기록하고 그보다 낮은 것은 고려하지 않는 방법
K개 이상인 알파벳의 첫 자리부터 해당 알파벳이 K개 나올때까지 문자열을 검증할 수 있는데...
그 중 가장 짧은 문자열인지는 어떻게 검증할 것인가 => answer1을 매번 계산하며 비교할 수 있다.
예로 a를 K개 이상 갖고있는 연속된 문자열의 길이를 구하고, b를 K개 이상 가진 연속된 문자열의 길이를 구한다... K개 이상인 알파벳 전부다.
4번 조건은 이미 구해졌을 것 같긴 한데, 앞 뒤가 같은지는 매번 확인해야하나? 잠깐만, 애초에 앞 뒤가 다를 일이 있나?? 없네..?
그럼 그냥 K개를 정확히 포함하는 문자열 중 가장 짧은 것과, 가장 긴 것을 구하면 되는 것 아닌가?
"""
T = int(input())

for tc in range(T):
    W = input()
    K = int(input())
    # 소문자별로 index 위치를 배열 형태로 저장한다.
    alphabet_dict = dict()
    length = len(W)
    # K개 이상 등장한 알파벳들 저장
    over_K = []

    for i in range(length):
        # dictionary 있다면 index 위치를 배열에 추가한다.
        if W[i] in alphabet_dict.keys():
            alphabet_dict[W[i]].append(i)
        else:
            alphabet_dict[W[i]] = [i]
        # K개 이상일 경우 over_K에 저장
        if len(alphabet_dict[W[i]]) == K:
            over_K.append(W[i])

    # K개를 만족하는 알파벳이 없다면 -1
    if not over_K:
        print(-1)
    else:
        answers = []
        for alphabet in over_K:
            alphabet_cnt = len(alphabet_dict[alphabet])
            # K개인거랑 K개 넘는거랑 나눴는데 그러니까 시간만 더 잡아먹음
            for i in range(alphabet_cnt - K + 1):
                char_length = alphabet_dict[alphabet][i + K - 1] - alphabet_dict[alphabet][i] + 1
                answers.append(char_length)
        print(min(answers), max(answers))

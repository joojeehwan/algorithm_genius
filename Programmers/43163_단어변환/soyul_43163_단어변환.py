def check(word1, word2):                        # 단어 두개가 다른 알파벳이 몇 개인지 체크하는 함수
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

def dfs(now_word, cnt, target, words, used):

    ans = 986523

    if cnt >= len(words):               # 체크한 숫자가 주어진 단어의 개수보다 많으면 불가능
        if now_word != target:
            return 0

    if now_word == target:              # 타켓단어가 만들어지면 끝
        # print(cnt)
        return cnt

    for i in range(len(words)):
        if used[i]:  # 이미 사용한 단어면 패스
            continue
        if check(now_word, words[i]) != 1:  # 다른 알파벳이 1개가 아니라면
            continue

        used[i] = 1
        ans = min(ans, dfs(words[i], cnt + 1, target, words, used))
        used[i] = 0

    return ans

def solution(begin, target, words):

    used = [0] * len(words)  # 단어 사용했는지 확인

    answer = dfs(begin, 0, target, words, used)
    return answer

""" 이전코드 (전역변수 사용)
def check(word1, word2):                        # 단어 두개가 다른 알파벳이 몇 개인지 체크하는 함수
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

ans = 9743235

def dfs(now_word, cnt, target, words, used):
    global ans

    if cnt >= len(words):               # 체크한 숫자가 주어진 단어의 개수보다 많으면 불가능
        if now_word != target:
            return

    if now_word == target:              # 타켓단어가 만들어지면 끝
        ans = min(ans, cnt)
        return

    for i in range(len(words)):
        if used[i]:  # 이미 사용한 단어면 패스
            continue
        if check(now_word, words[i]) != 1:  # 다른 알파벳이 1개가 아니라면
            continue

        used[i] = 1
        dfs(words[i], cnt + 1, target, words, used)
        used[i] = 0
    return ans

def solution(begin, target, words):

    used = [0] * len(words)  # 단어 사용했는지 확인

    answer = dfs(begin, 0, target, words, used)
    return answer

print(solution('hit', 'cog', ["dot", "dog", "lot", "log", "cog", "hot", "dat", "hat", "hit"]))
"""
def dfs(name, cnt, answer=0, now=0):
    global ans
    if name[now] != 'A':
        # 위아래로 움직이기
        big_target, small_target = ord(name[now]), ord(name[now]) - 26
        target = min(big_target - ord('A'), abs(small_target - ord('A')))
        answer += target
        name = name[:now] + 'A' + name[now + 1:]
        cnt -= 1
    # 종료조건
    if not cnt:
        ans = min(ans, answer)
        return
    # 진행 중
    for i in range(1, len(name)):  # 오른쪽으로 이동
        if name[(now + i) % len(name)] != 'A':
            dfs(name, cnt, answer + i, (now + i) % len(name))
            break
    for i in range(1, len(name)):  # 왼쪽으로 이동
        if name[now - i] != 'A':
            if now - i < 0:  # 오른쪽 끝으로 이동
                dfs(name, cnt, answer + i, len(name) + (now - i))
            else:
                dfs(name, cnt, answer + i, now - i)
            break
    return


def solution(name):
    global ans
    ans = 987654321
    cnt = len(name) - name.count('A')  # 바꿔야 할 글자 수
    dfs(name, cnt)
    return ans


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))
print(solution("JAAAAAAAAAAAABAAA"))
print(solution("A"))
print(solution("ABABAAAAAAABA"))

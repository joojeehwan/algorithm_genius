import sys
input = sys.stdin.readline

# 전체 문자열에서 단 하나만 제거할 수 있으니
# 양 끝에서부터 시작해서 비교하고,
# 불일치하게 되어 그 하나를 제거한 이후에는 완벽한 회문인지를 판별

# 제거 후 완벽한 회문인지를 판별하는 함수
def nowornever(s, l, r):
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        else:
            return 2
    return 1

for t in range(int(input())):
    s = input().rstrip()
    l = 0               # left 인덱스
    r = len(s) - 1      # right 인덱스
    isPalin = 0         # 회문 판단 플래그
    while l < r:
        if s[l] == s[r]:    # 만약 양 끝단이 일치한다면
            l += 1
            r -= 1
            continue        # 하던대로 계속 진행
        else:
            isPalin = 2     # 일단 남은 문자열은 회문이 아니라고 기본 전제
            if s[l+1] == s[r]:  # 왼쪽 끝을 버린 문자열의 양 끝이 일치하면
                isPalin = nowornever(s, l + 1, r) # 판별
            if s[l] == s[r-1]:  # 오른쪽 끝을 버린 문자열의 양 끝이 일치하면
                isPalin = min(isPalin, nowornever(s, l, r - 1)) # 판별 후 이전 판별값과 비교
            break
    
    print(isPalin) # 판별값 출력
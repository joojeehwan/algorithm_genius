S, P = map(int, input().split())
pwd = input()
_A, _C, _G, _T = map(int, input().split())

cnt = {"A": 0, "C": 0, "G": 0, "T": 0}
answer, start = 0, 0

# 초기 P글자
for i in range(P):
    cnt[pwd[i]] += 1


while True:
    if cnt["A"] >= _A and cnt["C"] >= _C and cnt["G"] >= _G and cnt["T"] >= _T:
        answer += 1
    if start == S - P:
        break
    cnt[pwd[start]] -= 1
    cnt[pwd[start+P]] += 1
    start += 1

print(answer)

from itertools import combinations
n = int(input())
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
comb = []
for i in range(1, 11):                          # 가능한 모든 조합을 만들어줌
    lst = list(combinations(num, i))
    for l in lst:
        sort_num = sorted(l, reverse=True)
        pos = ''
        for s in sort_num:
            pos += str(s)
        comb.append(int(pos))
comb.sort()

if n >= len(comb):
    print(-1)
else:
    print(comb[n-1])

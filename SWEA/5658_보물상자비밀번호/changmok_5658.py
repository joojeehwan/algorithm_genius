import sys
input = sys.stdin.readline

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    dial = input().rstrip()
    lnth = len(dial)
    numlen = lnth // 4

    nums = set()
    for start in range(numlen):
        lp = start
        rp = lp + numlen
        while rp <= lnth:
            nums.add(dial[lp:rp])
            lp = rp
            rp += numlen
        leftover = dial[lp:]
        leftover += dial[0:start]
        if leftover:
            nums.add(leftover)

    nums = sorted(list(nums), reverse=True)
    pick = nums[k-1]

    converted = 0
    mp = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7':7, '8':8,'9':9,'A':10,'B':11,'C':12,'D':13, 'E':14, 'F':15}

    for i in range(numlen):
        converted += mp[pick[numlen-i-1]] * (16 ** i)

    print(f'#{t} {converted}')